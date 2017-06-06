from django.db import models
import json
# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=70)
	def __unicode__(self):
		return '%s' % (self.user_name)

class Role(models.Model):
	id = models.AutoField(primary_key=True)
	role_name = models.CharField(max_length=70)
	def __unicode__(self):
		return '%s' % (self.role_name)
	
class Permission(models.Model):
	id = models.AutoField(primary_key=True)
	permission_name = models.CharField(max_length=70)
	def __unicode__(self):
		return '%s' % (self.permission_name)


class user_map_role(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User)
	role_id  = models.ForeignKey(Role)
	def __unicode__(self):
		return '%s' % (self.role_id)
	
class role_map_permission(models.Model):
	id = models.AutoField(primary_key=True)
	role_id  = models.ForeignKey(Role)
	permission_id  = models.ForeignKey(Permission)
	def __unicode__(self):
		return '%s' % (self.permission_id)
