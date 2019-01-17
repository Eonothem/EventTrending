from django.db import models


# Create your models here.

class NewsRecords(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200, primary_key=True)
    pub_time = models.DateTimeField('date published')
    content = models.TextField()
    keyword = models.CharField(max_length=100)

