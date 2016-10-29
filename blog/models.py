from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

    def __str__(self):
        return self.title