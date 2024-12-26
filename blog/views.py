from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import BlogSerializer
from .models import Blog
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create and list all blog posts
class CreateBlogView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Retrieve, update and delete a blog post
class RetrieveBlogView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CreatePostView(CreateAPIView):
    serializer_class = BlogSerializer

    def post(self, request):
        if Blog.objects.filter(title=request.data['title']).exists():
            return HttpResponse({
                'message': 'Blog with this title already exists'
            }, status=400)

        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({
                'message': 'Blog created successfully',
                'data': serializer.data
            }, status=201)
        return HttpResponse({
            'message': 'Invalid data',
            'errors': serializer.errors
        }, status=400)