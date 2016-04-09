from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from entities.serializers import *
from entities.models import *

# Create your views here.
class CreativeInfo(APIView):
  def post(self, request, format=None):
    serializer = CreativeSerializer(data=request.data)
    if serializer.is_valid():
      creative = serializer.save()
      return Response({'id': creative.id})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, format=None):
    creatives = Creative.objects.all()
    serializer = CreativeSerializer(creatives, many=True)
    return Response(serializer.data)

class CreativeSkills(APIView):
  def post(self, request, pk, format=None):
    creative = Creative.objects.get(id=pk)
    serializer = CreativeSkillSerializer(data=request.data, many=True)
    if serializer.is_valid():
      serializer.save(creative=creative)
    return Response({'id': pk})

  def get(self, request, pk, format=None):
    creative = Creative.objects.get(id=pk)
    skills = creative.creativeskill_set.all()
    return Response(CreativeSkillSerializer(skills, many=True).data)

class CreativeTypes(APIView):
  def post(self, request, pk, format=None):
    creative = Creative.objects.get(id=pk)
    serializer = CreativeTypeSerializer(data=request.data, many=True)
    if serializer.is_valid():
      serializer.save(creative=creative)
    return Response({'id': pk})

  def get(self, request, pk, format=None):
    creative = Creative.objects.get(id=pk)
    types = creative.creativetype_set.all()
    return Response(CreativeTypeSerializer(types, many=True).data)

class ProjectSkills(APIView):
  def post(self, request, pk, format=None):
    project = Project.objects.get(id=pk)
    serializer = ProjectSkillSerializer(data=request.data, many=True)
    if serializer.is_valid():
      serializer.save(project=project)
    return Response({'id': pk})

  def get(self, request, pk, format=None):
    project = Project.objects.get(id=pk)
    skills = project.projectskill_set.all()
    return Response(ProjectSkillSerializer(skills, many=True).data)

class OrganizationInfo(APIView):
  def post(self, request, format=None):
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
      organization = serializer.save()
      return Response({'id': organization.id})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, format=None):
    orgs = Organization.objects.all()
    return Response(OrganizationSerializer(orgs, many=True).data)

class CreateProject(APIView):
  def post(self, request, pk, format=None):
    serializer = CreateProjectSerializer(data=request.data)
    if serializer.is_valid():
      organization = Organization.objects.get(id=pk)
      project = serializer.save(org=organization)
      return Response({'id': project.id})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectInfo(APIView):
  def get(self, request, format=None):
    projects = Project.objects.all()
    return Response(ProjectSerializer(projects, many=True).data)

class CreativeSearch(APIView):
  def post(self, request, format=None):
    serializer = SearchSerializer(data=request.data)
    if serializer.is_valid():
      search = serializer.data['search'].upper()
      matched = []
      skills = CreativeSkill.objects.all()
      for skill in skills:
        if skill.value.upper() == search:
          matched.append(skill.creative)

      if len(matched) == 0:
        creatives = Creative.objects.all()
        for creative in creatives:
          if search in creative.name.upper() or creative.name.upper() in search:
            matched.append(creative)
      return Response(CreativeSerializer(matched, many=True).data)

    return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

class OrganizationSearch(APIView):
  def post(self, request, format=None):
    serializer = SearchSerializer(data=request.data)
    if serializer.is_valid():
      search = serializer.data['search'].upper()
      matched = []
      orgs = Organization.objects.all()
      for org in orgs:
        if org.category.upper() == search:
          matched.append(org)

      if len(matched) == 0:
        for org in orgs:
          if search in org.name.upper() or org.name.upper() in search:
            matched.append(org)
      return Response(OrganizationSerializer(matched, many=True).data)

    return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

class ProjectSearch(APIView):
  def post(self, request, format=None):
    serializer = SearchSerializer(data=request.data)
    if serializer.is_valid():
      search = serializer.data['search'].upper()
      matched = []
      skills = ProjectSkill.objects.all()
      for skill in skills:
        if skill.value.upper() == search:
          matched.append(skill.project)

      if len(matched) == 0:
        projects = Project.objects.all()
        for project in projects:
          if search in project.name.upper() or project.name.upper() in search:
            matched.append(project)
      return Response(ProjectSerializer(matched, many=True).data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreativeMessages(APIView):
  def post(self, request, pk, format=None):
    serializer = CreateOrganizationMessageSerializer(data=request.data)
    if serializer.is_valid():
      organization = Organization.objects.get(id=serializer.data['organization'])
      creative = Creative.objects.get(id=pk)
      value = serializer.data['value']
      msg = OrganizationMessage(value=value, to=organization, sender=creative)
      msg.save()
      return Response({'success': True})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, pk, format=None):
    creative = Creative.objects.get(id=pk)
    messages = creative.creativemessage_set.all()
    return Response(CreativeMessageSerializer(messages, many=True).data)

class OrganizationMessages(APIView):
  def post(self, request, pk, format=None):
    serializer = CreateCreativeMessageSerializer(data=request.data)
    if serializer.is_valid():
      value = serializer.data['value']
      creative = Creative.objects.get(id=serializer.data['creative'])
      organization = Organization.objects.get(id=pk)
      msg = CreativeMessage(value=value, to=creative, sender=organization)
      msg.save()
      return Response({'success': True})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, pk, format=None):
    org = Organization.objects.get(id=pk)
    messages = org.organizationmessage_set.all()
    return Response(OrganizationMessageSerializer(messages, many=True).data)

