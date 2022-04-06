from django.shortcuts import render
from django.http import HttpResponse, Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Blog
from .serializers import BlogListSerializer, BlogDetailSerializer

def index(request):
    blog = Blog.objects.get(id=1)
    print(blog.content)
    return render(request, "main/index.html", {'blog': blog})
    
    
class BlogList(APIView):
     
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True, context={'request': request})
        return Response(serializer.data)

        
        
class BlogDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data)
