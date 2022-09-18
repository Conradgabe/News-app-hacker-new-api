from django.db import models

class News(models.Model):
    item_id = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.item_id
