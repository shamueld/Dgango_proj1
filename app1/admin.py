# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app1.models import Topic,Webpage,AccessRecord,User

# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
