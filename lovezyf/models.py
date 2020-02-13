from django.db import models
from django.contrib import admin
from django import forms
from datetime import datetime

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=300)
    time = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.message


admin.site.register([Comment, ])