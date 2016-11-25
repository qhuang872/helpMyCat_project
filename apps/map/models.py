# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

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
    last_name = models.CharField(max_length=30)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class ForumForum(models.Model):
    forum = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_forum'


class ForumPost(models.Model):
    post = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thread = models.ForeignKey('ForumThread', models.DO_NOTHING)
    writer = models.ForeignKey('LoginregisterUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forum_post'


class ForumThread(models.Model):
    thread = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    creator = models.ForeignKey('LoginregisterUser', models.DO_NOTHING)
    forum = models.ForeignKey(ForumForum, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forum_thread'


class LoginregisterUser(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'loginRegister_user'


class Pets(models.Model):
    impound_no = models.TextField(blank=True, null=True)
    animal_id = models.TextField(db_column='Animal_ID', blank=True, null=True)  # Field name made lowercase.
    data_source = models.TextField(db_column='Data_Source', blank=True, null=True)  # Field name made lowercase.
    record_type = models.TextField(db_column='Record_Type', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    current_location = models.TextField(db_column='Current_Location', blank=True, null=True)  # Field name made lowercase.
    animal_name = models.TextField(db_column='Animal_Name', blank=True, null=True)  # Field name made lowercase.
    animal_type = models.TextField(blank=True, null=True)
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    animal_gender = models.TextField(db_column='Animal_Gender', blank=True, null=True)  # Field name made lowercase.
    animal_breed = models.TextField(db_column='Animal_Breed', blank=True, null=True)  # Field name made lowercase.
    animal_color = models.TextField(db_column='Animal_Color', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    date_type = models.TextField(db_column='Date_Type', blank=True, null=True)  # Field name made lowercase.
    obfuscated_address = models.TextField(db_column='Obfuscated_Address', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
    jurisdiction = models.TextField(blank=True, null=True)
    obfuscated_latitude = models.TextField(blank=True, null=True)
    obfuscated_longitude = models.TextField(blank=True, null=True)
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    image_alt_text = models.TextField(blank=True, null=True)
    location_for_map = models.TextField(blank=True, null=True)
    memo = models.TextField(db_column='Memo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pets'
