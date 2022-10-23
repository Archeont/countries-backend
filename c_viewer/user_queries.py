from django.contrib.auth.models import User
User.objects.all()
piotr = User.objects.create_user('piotr', password='regpasswd')
piotr.username
piotr.password
from django.contrib.auth import authenticate
authenticate(username='piotr', password='correctpasswd')
authenticate(username='piotr', password='wrongpasswd')