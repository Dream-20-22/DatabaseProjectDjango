# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CmsSiteBooking(models.Model):
    customers = models.ForeignKey('CmsSiteCustomer', models.DO_NOTHING)
    screening = models.ForeignKey('CmsSiteScreening', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_site_booking'


class CmsSiteCustomer(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'cms_site_customer'


class CmsSiteFilm(models.Model):
    name = models.CharField(max_length=45)
    length_min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_site_film'


class CmsSiteReservedSeat(models.Model):
    booking = models.ForeignKey(CmsSiteBooking, models.DO_NOTHING)
    seat = models.ForeignKey('CmsSiteSeat', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_site_reserved_seat'


class CmsSiteRoom(models.Model):
    name = models.CharField(max_length=45)
    no_seats = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_site_room'


class CmsSiteScreening(models.Model):
    start_time = models.DateTimeField()
    film = models.ForeignKey(CmsSiteFilm, models.DO_NOTHING)
    room = models.ForeignKey(CmsSiteRoom, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_site_screening'


class CmsSiteSeat(models.Model):
    row_id = models.CharField(max_length=1)
    seat_number = models.IntegerField()
    room = models.ForeignKey(CmsSiteRoom, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_site_seat'


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=32, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=32)
    building = models.CharField(max_length=32, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Instructor(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=32, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'


class Prereq(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, primary_key=True,related_name="course_course")
    prereq = models.ForeignKey(Course, models.DO_NOTHING,related_name="course_prereq")

    class Meta:
        managed = False
        db_table = 'prereq'
        unique_together = (('course', 'prereq'),)


class Section(models.Model):
    course_id = models.CharField(max_length=15, blank=True, null=True)
    sec_id = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    building = models.CharField(max_length=15, blank=True, null=True)
    room = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    tot_cred = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Takes(models.Model):
    id = models.ForeignKey(Student, models.DO_NOTHING, db_column='id', primary_key=True,related_name="student_id")
    course = models.ForeignKey(Section, models.DO_NOTHING,related_name="section_course")
    sec = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True,related_name="section_sec")
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', blank=True, null=True,related_name="section_semester")
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year',related_name="section_year")
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takes'
        unique_together = (('id', 'course', 'year'),)


class Teaches(models.Model):
    id = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='id',primary_key=True)
    course = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True,related_name="teaches_course")
    sec = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True,related_name="teaches_sec")
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', blank=True, null=True,related_name="teaches_semester")
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', blank=True, null=True,related_name="teaches_year")

    class Meta:
        managed = False
        db_table = 'teaches'
