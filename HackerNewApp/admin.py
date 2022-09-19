from django.contrib import admin

from .models import News, Story, Comment, Ask, Job, Poll, Pollopt

admin.site.register(News)
admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Ask)
admin.site.register(Job)
admin.site.register(Poll)
admin.site.register(Pollopt)
