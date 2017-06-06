from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/(?P<userid>\d+)/$', views.UserView.as_view()),
    url(r'^checkpermission/?userid=(?P<userid>\d+)&permissionid=(?P<permissionid>\d+)', views.CheckpermissionView.as_view()),
    url(r'^user/permissions/(?P<permissionid>\d+)/$', views.DeletePermissionView.as_view()),
    # url(r'^>/roles/<roleid>', views.RolesView.as_view()),
    # url(r'^/permissions/<permission_id>', views.PermissionsView.as_view()),
]