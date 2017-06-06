from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Role, Permission, user_map_role, role_map_permission
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, user_map_roleSerializer, role_map_permissionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.


class UserView(APIView):
	def get(self, request, userid):
		#print "jmk,l"
		roles = user_map_role.objects.filter(user_id = userid)
		permission = role_map_permission.objects.filter(role_id__in = roles.values_list('id'))
		serializer = role_map_permissionSerializer(permission, many = True)
		return Response(serializer.data)


class CheckpermissionView(APIView):
	def get(self, request, userid, permissionid):
		#print "jmk,l"
		flag=0
		flag1=0
		if User.objects.get(id = userid).exist():
			print "t"
			flag=1

		if Permission.objects.get(id = permissionid).exist():
			print "t1"
			flag1=1

		if flag1==1 and flag==1:
			print "True"

		else:
			print "flase"


class DeletePermissionView(APIView):
	def get(self, request, permissionid):
		Permission.objects.get(id = permissionid).delete()
		role_map_permission.objects.filter(permission_id = permissionid).delete()
		p = Permission.objects.all()
		serializer = PermissionSerializer(p, many = True)
		return Response(serializer.data)
