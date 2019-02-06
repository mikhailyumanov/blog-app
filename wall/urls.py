from django.urls import path

from . import views

app_name = 'wall'
urlpatterns = [
    path('<int:post_id>/', views.detail, name='detail'),
    path('post/', views.post, name='post'),
    path('', views.index, name='index'),
]
