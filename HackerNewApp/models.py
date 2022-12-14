from django.db import models
from django.db.models import Q

class NewsQuerySet(models.QuerySet):
    def is_type_of(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(item_id__icontains=query) | Q(author__icontains=query)
        qs = self.is_type_of().filter(lookup)
        return qs


class NewsManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return NewsQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query)


class News(models.Model):

    TYPE_CHOICES = (
        ('story', 'story'),
        ('comment', 'comment'),
        ('ask', 'ask'),
        ('job', 'job'),
        ('poll', 'poll'),
        ('pollopt', 'pollopt'),
    )

    author = models.CharField(max_length=35, null=True)
    item_id = models.CharField(max_length=25)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)
    time = models.CharField(max_length=40, null=True)
    text = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    poll = models.IntegerField(blank=True, null=True)
    kids = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    parts = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=True)

    # objects = NewsManager()

    def __str__(self):
        return self.item_id

    

# class Author(models.Model):
#     username = models.CharField(max_length=25)

class Story(models.Model):

    TYPE_CHOICES = (
        ('story', 'story'),
        ('comment', 'comment'),
        ('ask', 'ask'),
        ('job', 'job'),
        ('poll', 'poll'),
        ('pollopt', 'pollopt'),
    )
    
    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    descendants = models.IntegerField()
    kids = models.TextField()
    score = models.IntegerField()
    time = models.CharField(max_length=40)
    title = models.CharField(max_length=250)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)
    url = models.CharField(max_length=200, blank=True)
    public = models.BooleanField(default=True)

    objects = NewsManager()

    def __str__(self):
        return f"{self.author} - {self.title}"

class Comment(models.Model):

    TYPE_CHOICES = (
        ('story', 'story'),
        ('comment', 'comment'),
        ('ask', 'ask'),
        ('job', 'job'),
        ('poll', 'poll'),
        ('pollopt', 'pollopt'),
    )

    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    text = models.TextField()
    kids = models.TextField()
    parent = models.IntegerField()
    time = models.CharField(max_length=40)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.author} - {self.type_of}"

class Ask(models.Model):
    
    TYPE_CHOICES = (
        ('story', 'story'),
        ('comment', 'comment'),
        ('ask', 'ask'),
        ('job', 'job'),
        ('poll', 'poll'),
        ('pollopt', 'pollopt'),
    )

    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    text = models.TextField()
    descendants = models.IntegerField()
    kids = models.TextField()
    score = models.IntegerField()
    time = models.CharField(max_length=40)
    title = models.CharField(max_length=250)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.author} - {self.title}"

class Job(models.Model):

    TYPE_CHOICES = (
        ('story', 'story'),
        ('comment', 'comment'),
        ('ask', 'ask'),
        ('job', 'job'),
        ('poll', 'poll'),
        ('pollopt', 'pollopt'),
    )

    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    text = models.TextField()
    score = models.IntegerField()
    time = models.CharField(max_length=40)
    title = models.CharField(max_length=250)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.author} - {self.title}"

class Poll(models.Model):

    TYPE_CHOICES = (
        ('story', 'story'),
        ('comment', 'comment'),
        ('ask', 'ask'),
        ('job', 'job'),
        ('poll', 'poll'),
        ('pollopt', 'pollopt'),
    )

    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    descendants = models.IntegerField()
    kids = models.TextField()
    parts = models.TextField()
    score = models.IntegerField()
    text = models.TextField()
    time = models.CharField(max_length=40)
    title = models.CharField(max_length=250)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.author} - {self.title}"

class Pollopt(models.Model):

    TYPE_CHOICES = (
        ('story', 'story'),
        ('comment', 'comment'),
        ('ask', 'ask'),
        ('job', 'job'),
        ('poll', 'poll'),
        ('pollopt', 'pollopt'),
    )

    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    poll = models.IntegerField()
    text = models.TextField()
    score = models.IntegerField()
    time = models.CharField(max_length=40)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.author} - {self.poll}"
