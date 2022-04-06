from rest_framework import serializers
from django_quill.drf.fields import QuillHtmlField, QuillPlainField

from .models import Blog


class BlogListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Blog
        fields = ["id", "url", "title", "created", "truncated"]
        


class BlogDetailSerializer(serializers.ModelSerializer):
    content = QuillHtmlField()
    
    class Meta:
        model = Blog
        fields = ["id", "title", "content", "created"]
        