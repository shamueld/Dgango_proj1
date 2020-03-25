import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_templates.settings')

import django
django.setup()

from faker import Faker
import random
from app1.models import User

fake = Faker()

def populate_users(N=5):
    for _ in range(N):
        
        f_name = fake.first_name()
        l_name = fake.last_name()
        email_id = fake.email()

        user = User.objects.get_or_create(first_name=f_name, last_name=l_name, email=email_id)[0]
        user.save()


if __name__ == "__main__":
    print("Populating users...")
    # populate_users(10)
    print("Users created")

