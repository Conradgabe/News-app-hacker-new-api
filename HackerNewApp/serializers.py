from rest_framework import serializers

from .models import News, Story, Comment, Ask, Job, Poll, Pollopt

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"