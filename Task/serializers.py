from rest_framework import serializers
from .models import User, Role, Permission, user_map_role, role_map_permission

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permission
		fields = '__all__'


class user_map_roleSerializer(serializers.ModelSerializer):
	class Meta:
		model = user_map_role
		fields = '__all__'


class role_map_permissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = role_map_permission
		fields = '__all__'
