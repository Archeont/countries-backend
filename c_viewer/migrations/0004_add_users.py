from django.contrib.auth.models import User
from c_viewer.models import Profile

from django.db import migrations


def combine_names(apps, schema_editor):
    u = User.objects.create_user(username='dorian', password='admin', is_superuser=1)
    Profile.objects.create(user=u, countries_count=0)


class Migration(migrations.Migration):
    dependencies = [
       ('c_viewer', '0003_profile'),
    ]
    operations = [
       migrations.RunPython(combine_names),
    ]
