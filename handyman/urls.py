from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]

# Masters
urlpatterns += [
    path('masters/', views.masters, name='masters'),
    path('masters/<slug:skill_slug>/', views.show_masters, name='masters_type'),
    path('masters/<slug:skill_slug>/<uuid:master_id>', views.show_master, name='master_page'),
]

# Tasks
urlpatterns += [
    path('add_task/', views.add_task, name='add_task'),
    path('task/take/<uuid:task_id>/', views.take_task, name='take_task'),
    path('task/complete/<uuid:task_id>/', views.complete_task, name='complete_task'),
    path('task/delete/<uuid:task_id>/', views.delete_task, name='delete_task'),
    path('tasks/', views.masterTasks, name='tasks'),

]

# Feedbacks
urlpatterns += [
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('feedbacks/add_feedback/', views.feedback_view, name='add_feedback'),
    path('feedbacks/delete/<uuid:feedback_id>/', views.delete_feedback, name='delete_feedback'),

]

# Auth
urlpatterns += [
    path('register/', views.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='registration/login.html', extra_context={'title': 'Вход'}),
         name='login'),
    path('logout/', views.custom_logout, name='logout'),

]

# Account
urlpatterns += [
    path('account/', views.account, name='account'),

]

# Admin panel
urlpatterns += [
    path('adminpanel/', views.adminPanel, name='adminpanel'),
    path('adminpanel/delete_masters/<slug:skill_slug>/', views.delete_masters, name='delete_masters'),
    path('adminpanel/delete_masters/<slug:skill_slug>/<slug:master_id>', views.delete_master, name='delete_master'),
    path('adminpanel/add_master/<slug:skill_slug>/', views.add_master, name='add_master'),
    path('adminpanel/delete_portfolio/<slug:master_id>', views.delete_portfolio, name='delete_portfolio'),
    path('adminpanel/add_portfolio/<slug:master_id>', views.add_portfolio, name='add_portfolio'),
]
