from django.urls import path

from .views import index, BlogList, BlogDetail
urlpatterns = [
    path("", index),
    
    #API views
    
    path("blogs/", BlogList.as_view(), name="blog-list"),
    path("blog/<int:pk>", BlogDetail.as_view(), name="blog-detail"),
    
]