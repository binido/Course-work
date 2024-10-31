from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('masters/', views.masters, name='masters'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('masters/<slug:skill_slug>/', views.show_masters, name='masters_type'),
    path('masters/<slug:skill_slug>/<uuid:master_id>', views.show_master, name='master_page'),
    path('register/', views.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='registration/login.html', extra_context={'title': 'Вход'}),
         name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('account/', views.account, name='account'),
    path('account/adminpanel/', views.adminPanel, name='adminpanel'),
    path('account/tasks/', views.masterTasks, name='tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('task/take/<uuid:task_id>/', views.take_task, name='take_task'),
    path('task/complete/<uuid:task_id>/', views.complete_task, name='complete_task'),
    path('task/delete/<uuid:task_id>/', views.delete_task, name='delete_task'),

]
