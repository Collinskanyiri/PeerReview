from django.contrib import admin
from backend.models import Profile,Project,Like, Review


# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Like)
admin.site.register(Review)