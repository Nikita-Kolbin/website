from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', Post.as_view(), name='post'),
    path('category/<slug:category_slug>/', Category.as_view(), name='category'),
    path('form/', ShowForm.as_view(), name='form'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login')
]
