from django.db import models


class Post(models.Model):
    post_author = models.CharField(max_length=100)
    post_text = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')

    def get_preview(self):
        return self.post_text[:100]

    def is_large(self):
        return len(self.post_text) > 100

    def __str__(self):
        return "<%s - %s>" % (self.post_author, self.pub_date)
