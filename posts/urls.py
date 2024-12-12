from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.post_list, name='list'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('post/new/', views.post_create, name='create'),
    path('post/<int:pk>/edit/', views.post_edit, name='edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='delete')
]
