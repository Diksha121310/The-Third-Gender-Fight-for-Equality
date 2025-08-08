
from django.db import models


class Member(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    age = models.IntegerField()
    education = models.TextField()
    skills = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    address = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = 'tblMRegistration'


class Volunteer(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    age = models.IntegerField()
    education = models.TextField()
    skills = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    address = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = 'tblVRegistration'


class Employer(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    company = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    address = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = 'tblERegistration'


class Event(models.Model):
    id = models.TextField(primary_key=True)
    vid = models.TextField()
    name = models.TextField()
    details = models.TextField()

    class Meta:
        db_table = 'tblEvent'


class Video(models.Model):
    id = models.TextField(primary_key=True)
    vid = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = 'tblVideo'


class Adoption(models.Model):
    id = models.TextField(primary_key=True)
    description = models.TextField()
    nid = models.TextField()
    nname = models.TextField()
    nmobile = models.TextField()
    naddress = models.TextField()

    class Meta:
        db_table = 'tblAdoption'


class ARequest(models.Model):
    id = models.TextField(primary_key=True)
    date = models.TextField()
    aid = models.TextField()
    description = models.TextField()
    mid = models.TextField()
    name = models.TextField()
    mobile = models.TextField()
    address = models.TextField()
    status = models.TextField()
    nid = models.TextField()

    class Meta:
        db_table = 'tblARequest'


class Job(models.Model):
    id = models.TextField(primary_key=True)
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
    salary = models.TextField()
    eid = models.TextField()
    company = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    address = models.TextField()

    class Meta:
        db_table = 'tblJob'


class JRequest(models.Model):
    id = models.TextField(primary_key=True)
    date = models.TextField()
    jid = models.TextField()
    title = models.TextField()
    description = models.TextField()
    salary = models.TextField()
    eid = models.TextField()
    company = models.TextField()
    eemail = models.TextField()
    emobile = models.TextField()
    eaddress = models.TextField()
    mid = models.TextField()
    mname = models.TextField()
    mmobile = models.TextField()
    maddress = models.TextField()
    status = models.TextField()

    class Meta:
        db_table = 'tblJRequest'


class NGO(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    address = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = 'tblNRegistration'

