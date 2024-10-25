from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('masters/', views.masters, name='masters'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('masters/<slug:skill_slug>/', views.show_master, name='masters_type'),
]