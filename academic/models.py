from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .utils import generate_random_base64, person_picture_path


# Create your models here.
"""
Documents Models
"""
class DocumentType(models.Model):
    name = models.CharField(max_length=50)


class Document(models.Model):
    code = models.CharField(max_length=15)
    description = models.TextField()
    attachment = models.URLField()
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    
    # Polymorphic Relationship
    documentable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    documentable_id = models.PositiveIntegerField()
    documentable_object = GenericForeignKey('documentable_type', 'documentable_id')


    def save(self, *args, **kwargs):
        # Generate Code
        if not self.code:
            self.code = generate_random_base64(15)

        super(Document, self).save(*args, **kwargs)


"""
User Models
"""
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.TextField()
    blood_group = models.CharField(max_length=5)
    dni = models.CharField(max_length=12)
    picture = models.ImageField(upload_to=person_picture_path)


class Phone(models.Model):
    number = models.CharField(max_length=10)
    description = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


"""
Academic
"""
class Project(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=150)
    description = models.TextField()


class Career(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)


class AdmissionType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class MemberType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class MemberPosition(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Member(models.Model):
    code = models.CharField(max_length=15)
    admission_date = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    admission_type = models.ForeignKey(AdmissionType, on_delete=models.CASCADE)
    member_type = models.ForeignKey(MemberType, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project)
    positions = models.ManyToManyField(
        MemberPosition, 
        through='MemberPositionHistory', 
        through_fields=('member', 'member_position'),
    )


class MemberPositionHistory(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    member_position = models.ForeignKey(MemberPosition, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class ExtracurricularInformation(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=15)


class AcademicHistory(models.Model):
    semester = models.PositiveSmallIntegerField()
    year = models.PositiveIntegerField()
    subjects = models.ManyToManyField(Subject)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)