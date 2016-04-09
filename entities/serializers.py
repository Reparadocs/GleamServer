from rest_framework import serializers
from entities.models import *

class CreativeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Creative
    exclude = ()

class OrganizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organization
    exclude = ()

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    exclude = ()
    depth = 2

class CreateProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    exclude = ('org',)

class CreateCreativeMessageSerializer(serializers.Serializer):
  value = serializers.CharField(max_length=500)
  creative = serializers.IntegerField()

class CreateOrganizationMessageSerializer(serializers.Serializer):
  value = serializers.CharField(max_length=500)
  organization = serializers.IntegerField()

class CreativeMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreativeMessage
    exclude = ()
    depth = 2

class OrganizationMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrganizationMessage
    exclude = ()
    depth = 2

class SearchSerializer(serializers.Serializer):
  search = serializers.CharField(max_length=200)

class CreativeSkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreativeSkill
    exclude = ()
    depth = 2

class ProjectSkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectSkill
    exclude = ()
    depth = 2

class CreativeTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreativeType
    exclude = ()
    depth = 2