from django.contrib.auth.models import User


def create_user():
    Admin = User.objects.create_user('Admin', 'Admin@123')
    Professor = User.objects.create_user('Professor', 'Professor@123')
    Student = User.objects.create_user('Student', 'Student@123')

    # At this point, user is a User object that has already been saved
    # to the database. You can continue to change its attributes
    # if you want to change other fields.

    user.save()