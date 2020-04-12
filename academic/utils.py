import os


def person_picture_path(instance, filename):     
    # Default Path for Picture
    return 'persons/{0}/{1}'.format(instance.id, filename)


def generate_random_base64(length=12):
    return os.urandom(length).hex().upper()