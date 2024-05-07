
from django.urls import path
from kiran import views

urlpatterns = [
    path('', views.kiran),
    path('analysis',views.movie_analysis),
    path('genre',views.genre),
    path('review',views.review),
   
   
]