from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('category/<slug:category_slug>/', views.post_list, name='post_list_by_category'),
    path('donate/<int:post_id>/', views.donate_to_post, name='donate_to_post'),
    path('', views.home, name='home'),
]
