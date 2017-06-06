# Navya

## How to run

pip install django==1.8

pip install djangorestframework

pip install markdown       # Markdown support for the browsable API.

pip install django-filter  # Filtering support

cd Navya

python manage.py runserver #to runserver

1. Given user, return list of names of permissions that this user is entitled to

Ans url- localhost:8000/Task/user/(?P<userid>\d+)/

2.Given user and permission, return boolean if entitled or not

Ans url- 

3. Modify permissions of a role ex: http://<server>/roles/<roleid> POST_PARAM:{"permissions":["perm5"]} (POST Method)
Ans

4. Delete a permission ex: http://<server>/permissions/<permission_id> (DELETE Method).
Ans- localhost:8000/Task/user/permissions/(?P<permissionid>\d+)/
