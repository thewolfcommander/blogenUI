from django.urls import path
from . import views

urlpatterns =[
	path('categories/', views.categories, name='categories'),
	path('details/', views.details, name='details'),
	path('posts/', views.posts, name='posts'),
	path('profile/', views.profile, name='profile'),
	path('settings/', views.settings, name='settings'),
	path('users/', views.users, name='users'),
]