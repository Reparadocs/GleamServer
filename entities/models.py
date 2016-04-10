from __future__ import unicode_literals

from django.db import models

class Creative(models.Model):
  name = models.CharField(max_length=100)
  bio = models.CharField(max_length=500)
  picture = models.URLField()
  linkedin = models.CharField(max_length=200, blank=True, null=True)
  github = models.CharField(max_length=200, blank=True, null=True)
  dribbble = models.CharField(max_length=200,blank=True, null=True)
  behance = models.CharField(max_length=200,blank=True, null=True)
  active = models.BooleanField(default=True)

class Organization(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=500)
  picture = models.URLField()
  address = models.CharField(max_length=200,blank=True,  null=True)
  website = models.CharField(max_length=200,blank=True,  null=True)
  category = models.CharField(max_length=100)

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

class OrganizationSkill(models.Model):
  value = models.CharField(max_length=100)
  organization = models.ForeignKey(Organization)

class CreativeType(models.Model):
  value = models.CharField(max_length=100)
  creative = models.ForeignKey(Creative)
