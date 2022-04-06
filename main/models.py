import textwrap
from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content = QuillField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        
    @property
    def truncated(self):
        return textwrap.shorten(self.content.plain, width=300, placeholder='')