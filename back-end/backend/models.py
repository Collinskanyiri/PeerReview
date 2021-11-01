from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username=models.CharField(max_length=155)
    profile_photo=models.ImageField(upload_to='image')
    bio=models.CharField(max_length=255)
    projects=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username}Profile '

    def save_profile(self):
        self.save()

class Project(models.Model):
    project_name= models.CharField(max_length=100 )
    description=models.CharField(max_length=500)
    project_img=models.ImageField(upload_to='image')
    project_url=models.URLField(max_length=200)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.project_name

    def save_project(self):
        self.save()

class BlogPost(models.Model):
    topic = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)

    image = models.ImageField(upload_to='blog-photos', blank=True)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.topic} Blog | {self.title}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like: {self.user.username} | {self.blog.title}'

class Review(models.Model):
    Rating=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    ]
    project_perfomance=models.IntegerField(choices=Rating, default='1' )
    Design=models.IntegerField(choices=Rating, default='1' )
    Usability=models.IntegerField(choices=Rating, default='1' )
    Content=models.IntegerField(choices=Rating, default='1' )
    
    
