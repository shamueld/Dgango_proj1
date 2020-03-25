import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_templates.settings')

import django
django.setup()

from faker import Faker
import random
from app1.models import Topic, Webpage, AccessRecord



fake = Faker()
topics = ['Search','Social','Marketplace','News','Games','Music']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for _ in range(N):
        top = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populcating Data....")
    # populate(20)
    print("Population complete")