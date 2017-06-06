from django.contrib import admin
from .models import User, Role, Permission, user_map_role, role_map_permission
# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(role_map_permission)
admin.site.register(user_map_role)
