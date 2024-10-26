from django.shortcuts import get_object_or_404, render
from . import models
from .models import Master, Skills


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
