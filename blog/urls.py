from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/', views.Post.as_view(), name='post'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
]
