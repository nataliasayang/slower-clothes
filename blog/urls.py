from django.urls import path
from . import views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('about/', views.about_page, name='about_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('women/', views.women_brands, name='women_brands'),
    path('men/', views.men_brands, name='men_brands'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
