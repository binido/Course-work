from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from .models import Master, Skills, MasterTasks

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, MasterTasksForm

from django.contrib.auth import logout


def index(request):
    data = {"title": "Главная"}
    return render(request, "handyman/index.html", context=data)


def about(request):
    data = {"title": "О нас"}
    return render(request, "handyman/pages/static_pages/about.html", context=data)


def contacts(request):
    data = {"title": "Контакты"}
    return render(request, "handyman/pages/static_pages/contacts.html", context=data)


def feedbacks(request):
    data = {"title": "Отзывы"}
    return render(request, "handyman/pages/feedback_pages/feedbacks.html", context=data)


def masters(request):
    skills = Skills.objects.all()
    data = {
        "title": "Мастера",
        "skills": skills,
    }
    return render(request, "handyman/pages/master_pages/masters.html", context=data)


def show_masters(request, skill_slug):
    skill = get_object_or_404(Skills, slug=skill_slug)
    masters = Master.objects.filter(skill=skill)
    data = {
        "title": skill.cat_name,
        "skill": skill,
        "masters": masters,
    }
    return render(request, "handyman/pages/master_pages/mastertype.html", context=data)


def show_master(request, skill_slug, master_id):
    skill = get_object_or_404(Skills, slug=skill_slug)
    master = get_object_or_404(Master, id=master_id, skill=skill)
    data = {
        "title": master.name,
        "skill": skill,
        "master": master,
    }
    return render(request, "handyman/pages/master_pages/master.html", context=data)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ваш аккаунт создан!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'title': 'Регистрация'})


def custom_logout(request):
    logout(request)
    return redirect('index')


def account(request):
    user = request.user
    data = {"title": 'Личный кабинет',
            'user': user}

    return render(request, 'account/account.html', context=data)


def adminPanel(request):
    data = {
        'title': 'Админка'
    }

    return render(request, 'account/adminpanel.html', context=data)


def masterTasks(request):
    tasks_not_taken = MasterTasks.objects.filter(status='pending')
    tasks_in_progress = MasterTasks.objects.filter(status='in_progress')
    tasks_completed = MasterTasks.objects.filter(status='completed')

    data = {
        'title': 'Заказы',
        'tasks_not_taken': tasks_not_taken,
        'tasks_in_progress': tasks_in_progress,
        'tasks_completed': tasks_completed,
    }

    return render(request, 'account/mastetasks.html', context=data)


def add_task(request):
    if request.method == 'POST':
        form = MasterTasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'pending'
            task.save()
            return redirect('index')
    else:
        form = MasterTasksForm()

    return render(request, 'handyman/pages/task_pages/tasks.html', {'form': form, 'title': 'Вызвать мастера'})


def is_master(user):
    return user.groups.filter(name='master').exists()


def is_admin(user):
    return user.groups.filter(name='admin').exists()


@user_passes_test(is_master)
def take_task(request, task_id):
    task = get_object_or_404(MasterTasks, id=task_id)
    task.set_in_progress()
    return redirect('tasks')


@user_passes_test(is_master)
def complete_task(request, task_id):
    task = get_object_or_404(MasterTasks, id=task_id)
    task.set_completed()
    return redirect('tasks')


@user_passes_test(is_admin)
def delete_task(request, task_id):
    task = get_object_or_404(MasterTasks, id=task_id)
    task.delete()
    return redirect('tasks')
