from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name="index"),
    path('blog/', views.blog, name="post-list"),
    path('search/', views.search, name="search"),
    path('post/<id>/', views.post, name="post-detail"),
    path('create/', views.post_create, name="post-create"),
    path('post/<id>/update/', views.post_update, name="post-update"),
    path('post/<id>/delete', views.post_delete, name="post-delete"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.get_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('about/', views.AboutView, name="About"),
    path('contect/', views.ContectView, name="Contect"),
    path('team/', views.TeamView, name="Team")
]