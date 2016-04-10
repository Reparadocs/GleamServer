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


class CreateCreativeMessageSerializer(serializers.Serializer):
  value = serializers.CharField(max_length=500)
  to = serializers.IntegerField()

class CreateOrganizationMessageSerializer(serializers.Serializer):
  value = serializers.CharField(max_length=500)
  to = serializers.IntegerField()

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
  search = serializers.CharField(max_length=200, allow_blank=True)

class CreativeSkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreativeSkill
    exclude = ()
    depth = 2

class OrganizationSkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrganizationSkill
    exclude = ()
    depth = 2

class CreativeTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreativeType
    exclude = ()
    depth = 2