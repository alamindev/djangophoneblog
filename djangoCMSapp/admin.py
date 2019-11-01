from django.contrib import admin
from .models import Author, Category, Post, Comment, PostView, Contect, About
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Contect)
admin.site.register(About)

