from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),
    path('<int:blog_id>/comment', views.comment, name='comment')

]
