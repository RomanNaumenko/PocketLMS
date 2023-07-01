from django.contrib import admin

# Register your models here.
from lms_topics_and_logs.models import Topic
from lms_topics_and_logs.models import Entry
admin.site.register(Topic)
admin.site.register(Entry)