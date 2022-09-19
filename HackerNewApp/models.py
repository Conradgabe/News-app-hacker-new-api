from django.db import models

class News(models.Model):
    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)
    time = models.CharField(max_length=40)
    text = models.TextField(blank=True)
    parent = models.IntegerField(blank=True)
    poll = models.IntegerField(blank=True)
    kids = models.TextField(blank=True)
    url = models.URLField(max_length=200, blank=True)
    score = models.IntegerField(blank=True)
    title = models.CharField(max_length=250, blank=True)
    parts = models.TextField(blank=True)
    descendants = models.IntegerField(blank=True)

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
    url = models.URLField(max_length=200)

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
        return f"{self.author} - {self.title}"

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
