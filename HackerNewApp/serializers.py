from rest_framework import serializers

from .models import News, Story, Comment, Ask, Job, Poll, Pollopt

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ask
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"

class PolloptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pollopt
        fields = "__all__"