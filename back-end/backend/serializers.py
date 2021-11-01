from rest_framework import serializers
from backend.models import Profile, Project, Review, BlogPost,Like


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields=[
            'project_perfomance',
            'Design',
            'Usability',
            'Content',
        
        ]

class ProjectSerializer(serializers.ModelSerializer):
    proj_performance=ReviewSerializer(read_only=True, many=True)
    class Meta:
        model=Project
        fields=[
            'user',
            'project_name',
            'description',
            'project_img',
            'project_url',
            'proj_performance'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    projects=ProjectSerializer(read_only=True, many=True)
    class Meta:
        model=Profile
        fields=[
            'user',
            'username',
            'profile_photo',
            'bio',
            'projects',
        ]


class ShowBlogSerializer(serializers.ModelSerializer):
    
    Profile = ProfileSerializer

    class Meta:
        model = BlogPost
        exclude = ('content',)
        depth = 1


class CreateBlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogPost
        fields = '__all__'
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}


class DetailedBlogSerializer(serializers.ModelSerializer):
    
    Profile = ProfileSerializer

    class Meta:
        model = BlogPost
        fields = '__all__'
        depth = 1
class ShowLikeSerializer(serializers.ModelSerializer):
    
    Profile = ProfileSerializer
    blog = ShowBlogSerializer(help_text='blog serializer')

    class Meta:
        model = Like
        fields = '__all__'
        depth = 1


class CreateLikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'
