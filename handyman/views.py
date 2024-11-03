from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import get_object_or_404
from .models import Master, Skills, MasterTasks, Feedbacks, PortfolioImage, Service

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, MasterTasksForm, FeedbackForm, MasterForm, PortfolioImageForm

from django.contrib.auth import logout


def is_master(user):
    return user.groups.filter(name='master').exists()


def is_admin(user):
    return user.groups.filter(name='admin').exists()


def is_user(user):
    return user.groups.filter(name='user').exists()


def index(request):
    data = {"title": "Главная"}
    return render(request, "handyman/index.html", context=data)


def about(request):
    data = {"title": "О нас"}
    return render(request, "handyman/pages/static_pages/about.html", context=data)


def contacts(request):
    data = {"title": "Контакты"}
    return render(request, "handyman/pages/static_pages/contacts.html", context=data)


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
    services = Service.objects.filter(skill=skill)
    data = {
        "title": master.name,
        "skill": skill,
        "master": master,
        "services": services,

    }
    return render(request, "handyman/pages/master_pages/master.html", context=data)


@user_passes_test(is_admin)
def delete_portfolio(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    master.portfolio_images.all().delete()
    return redirect(master.get_absolute_url())


@user_passes_test(is_admin)
def add_portfolio(request, master_id):
    master = get_object_or_404(Master, id=master_id)

    if request.method == 'POST':
        form = PortfolioImageForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_image = form.save(commit=False)
            portfolio_image.master = master
            portfolio_image.save()
            return redirect(master.get_absolute_url())
    else:
        form = PortfolioImageForm()

    data = {
        'title': f'Портфолио для {master.name}',
        'form': form,
        'master': master,
    }
    return render(request, 'adminpanel/add_portfolio.html', context=data)


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


@login_required
def custom_logout(request):
    logout(request)
    return redirect('index')


@login_required
def account(request):
    user = request.user
    data = {"title": 'Личный кабинет',
            'user': user}

    return render(request, 'account/account.html', context=data)


@user_passes_test(is_admin)
def adminPanel(request):
    skills = Skills.objects.all()
    data = {
        'title': 'Админка',
        'skills': skills,
    }

    return render(request, 'adminpanel/adminpanel.html', context=data)


@user_passes_test(is_admin)
def delete_masters(request, skill_slug):
    skill = get_object_or_404(Skills, slug=skill_slug)
    masters = Master.objects.filter(skill=skill)
    data = {
        "title": f'Удалить {skill.name}',
        "skill": skill,
        "masters": masters,
    }
    return render(request, "adminpanel/delete_master.html", context=data)


@user_passes_test(is_admin)
def delete_master(request, skill_slug, master_id):
    skill = get_object_or_404(Skills, slug=skill_slug)
    master = get_object_or_404(Master, id=master_id, skill=skill)
    master.delete()
    return redirect('adminpanel')


@user_passes_test(is_admin)
def add_master(request, skill_slug):
    skill = get_object_or_404(Skills, slug=skill_slug)
    if request.method == 'POST':
        form = MasterForm(request.POST, request.FILES)
        if form.is_valid():
            master = form.save(commit=False)
            master.skill = skill
            master.save()
            return redirect(master.get_absolute_url())
    else:
        form = MasterForm()

    return render(request, 'adminpanel/add_master.html', {'form': form, 'skill': skill})


@user_passes_test(is_master)
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


@login_required
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


def feedbacks(request):
    feedback_list = Feedbacks.objects.all().order_by('-created_at')
    data = {
        "title": "Отзывы",
        "feedback_list": feedback_list
    }
    return render(request, "handyman/pages/feedback_pages/feedbacks.html", context=data)


@user_passes_test(is_user)
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.name = request.user.username
            feedback.save()
            return redirect('feedbacks')
    else:
        form = FeedbackForm()

    return render(request, 'handyman/pages/feedback_pages/feedback_form.html', {'form': form, 'title': 'Отзыв'})


@user_passes_test(is_admin)
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedbacks, id=feedback_id)
    feedback.delete()
    return redirect('feedbacks')
