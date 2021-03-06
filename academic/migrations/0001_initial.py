# Generated by Django 3.0.5 on 2020-04-12 22:41

import academic.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('admission_date', models.DateField()),
                ('admission_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.AdmissionType')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Career')),
            ],
        ),
        migrations.CreateModel(
            name='MemberPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('address', models.TextField()),
                ('blood_group', models.CharField(max_length=5)),
                ('dni', models.CharField(max_length=12)),
                ('picture', models.ImageField(upload_to=academic.utils.person_picture_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Person')),
            ],
        ),
        migrations.CreateModel(
            name='MemberPositionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Member')),
                ('member_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.MemberPosition')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='member_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.MemberType'),
        ),
        migrations.AddField(
            model_name='member',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academic.Person'),
        ),
        migrations.AddField(
            model_name='member',
            name='positions',
            field=models.ManyToManyField(through='academic.MemberPositionHistory', to='academic.MemberPosition'),
        ),
        migrations.AddField(
            model_name='member',
            name='projects',
            field=models.ManyToManyField(to='academic.Project'),
        ),
        migrations.CreateModel(
            name='ExtracurricularInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('attachment', models.URLField()),
                ('documentable_id', models.PositiveIntegerField()),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.DocumentType')),
                ('documentable_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveSmallIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.Member')),
                ('subjects', models.ManyToManyField(to='academic.Subject')),
            ],
        ),
    ]
