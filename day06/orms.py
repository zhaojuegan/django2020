import os
import sys,django
project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project)
sys.path.insert(0,project)
os.environ.setdefault('django_settings_module',
                      'django20.settings')
django.setup()

from day06.models import Users


user = Users.objects.create(
    name='demo',
    gender=2
)
print(user)
print(user.name)
print(user.gender)