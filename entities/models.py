from __future__ import unicode_literals

from django.db import models

class Creative(models.Model):
  name = models.CharField(max_length=100)
  bio = models.CharField(max_length=500)
  picture = models.URLField()
  linkedin = models.URLField(null=True)
  github = models.URLField(null=True)
  dribbble = models.URLField(null=True)
  behance = models.URLField(null=True)
  active = models.BooleanField(default=True)

class Organization(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=500)
  picture = models.URLField()
  address = models.CharField(max_length=200, null=True)
  website = models.URLField(null=True)
  category = models.CharField(max_length=100)

class Project(models.Model):
  name = models.CharField(max_length=200)
  picture = models.URLField()
  description = models.CharField(max_length=500)
  org = models.ForeignKey(Organization)

class OrganizationMessage(models.Model):
  value = models.CharField(max_length=500)
  to = models.ForeignKey(Organization)
  sender = models.ForeignKey(Creative)

class CreativeMessage(models.Model):
  value = models.CharField(max_length=500)
  to = models.ForeignKey(Creative)
  sender = models.ForeignKey(Organization)

class CreativeSkill(models.Model):
  value = models.CharField(max_length=100)
  creative = models.ForeignKey(Creative)

class ProjectSkill(models.Model):
  value = models.CharField(max_length=100)
  project = models.ForeignKey(Project)

class CreativeType(models.Model):
  value = models.CharField(max_length=100)
  creative = models.ForeignKey(Creative)
