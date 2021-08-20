from django.urls import path, include
from blog import views
urlpatterns = [
    #API for comment
    path('postComment', views.postComment, name="postComment"),
    
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),

]