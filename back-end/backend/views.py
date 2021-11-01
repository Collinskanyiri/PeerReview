from django.contrib.auth.models import User
from django.shortcuts import render
from backend.models import Profile, Project,Review,Like
from rest_framework import viewsets,permissions
from backend.serializers import ProfileSerializer, ProjectSerializer,UpdateProjectSerializer, ReviewSerializer,ShowProjectSerializer,CreateProjectSerializer,DetailedProjectSerializer,ShowLikeSerializer,CreateLikeSerializer
# Create your views here.
class ProfileApi(viewsets.ModelViewSet):
    
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.AllowAny]

class ProjectApi(viewsets.ModelViewSet):
    
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer,{
        'show': ShowProjectSerializer,
        'create': CreateProjectSerializer,
        'update': UpdateProjectSerializer,
        'detailed': DetailedProjectSerializer,
         }
    permission_classes=[permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        author = request.author
        request.data['author'] = author.pk
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        author = request.author
        request.data['author'] = author.pk
        return super().update(request, *args, **kwargs)

    
class ReviewApi(viewsets.ModelViewSet):
    
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[permissions.AllowAny]



class LikesApi(viewsets.ModelViewSet):

    serializer_class={
        'show': ShowLikeSerializer,
        'create': CreateLikeSerializer,
        'update': CreateLikeSerializer,
    }
    permission_classes=[permissions.AllowAny]
def get_queryset(self, username=None):
    if username is not None:
        user = Like.objects.get(username=username)
        queryset = Like.filter(author=user)
        return queryset
    else:
        queryset = Like.objects.all()
        return queryset
    