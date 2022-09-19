from django.db import models

class News(models.Model):
    author = models.CharField(max_length=35)
    item_id = models.CharField(max_length=25)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    parent = models.IntegerField()
    poll = models.IntegerField()
    kids = models.TextField()
    url = models.URLField(max_length=200)
    score = models.IntegerField()
    title = models.CharField(max_length=250)
    parts = models.TextField()
    descendants = models.IntegerField()

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
    time = models.DateTimeField(auto_now_add=True)
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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=25)
    text = models.TextField()
    kids = models.TextField()
    parent = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=25)
    text = models.TextField()
    descendants = models.IntegerField()
    kids = models.TextField()
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=25)
    text = models.TextField()
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=25)
    descendants = models.IntegerField()
    kids = models.TextField()
    parts = models.TextField()
    score = models.IntegerField()
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=25)
    poll = models.IntegerField()
    text = models.TextField()
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.author} - {self.poll}"
