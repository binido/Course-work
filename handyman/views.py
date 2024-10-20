from django.shortcuts import get_object_or_404, render
from handyman.models import Master, User, Feedback, Grade, Skills


mastersDb = [
    {
        "id": 1,
        "name": "Mastert1",
        "number": "111",
        "skill": "Slesar",
        "work_period": "sdf",
        "weekend": "sdf",
        "salary": "sdf",
        "grade": 1,
        "created_at": "sdf",
        "status": "sdf",
    },
    {
        "id": 2,
        "name": "Mastert2",
        "number": "222",
        "skill": "Plotnik",
        "work_period": "sdf",
        "weekend": "sdf",
        "salary": "sdf",
        "grade": 2,
        "created_at": "sdf",
        "status": "sdf",
    },
    {
        "id": 3,
        "name": "Mastert3",
        "number": "333",
        "skill": "Santehnic",
        "work_period": "sdf",
        "weekend": "sdf",
        "salary": "sdf",
        "grade": 3,
        "created_at": "sdf",
        "status": "sdf",
    },
    {
        "id": 4,
        "name": "Mastert4",
        "number": "444",
        "skill": "Mebelshic",
        "work_period": "sdf",
        "weekend": "sdf",
        "salary": "sdf",
        "grade": 4,
        "created_at": "sdf",
        "status": "sdf",
    },
    {
        "id": 5,
        "name": "Mastert5",
        "number": "555",
        "skill": "Gey",
        "work_period": "sdf",
        "weekend": "sdf",
        "salary": "sdf",
        "grade": 5,
        "created_at": "sdf",
        "status": "sdf",
    },
    {
        "id": 6,
        "name": "Mastert6",
        "number": "666",
        "skill": "Pidoras",
        "work_period": "sdf",
        "weekend": "sdf",
        "salary": "sdf",
        "grade": 6,
        "created_at": "sdf",
        "status": "sdf",
    },
]


def index(request):
    data = {"title": "Главная", "masters": mastersDb}
    return render(request, "handyman/index.html", context=data)


def about(request):
    data = {"title": "О нас"}
    return render(request, "handyman/pages/static_pages/about.html", context=data)


def contacts(request):
    data = {"title": "Контакты"}
    return render(request, "handyman/pages/static_pages/contacts.html", context=data)


def masters(request):
    data = {"title": "Мастера"}
    return render(request, "handyman/pages/master_pages/masters.html", context=data)


def show_master(request, skill_slug):
    # skill = get_object_or_404(Skills, slug=skill_slug)
    # masters = Master.objects.filter(skill=skill)

    # data = {"title": skill.name, "skill": skill, "masters": masters}
    data = {"title": skill_slug, "skill": skill_slug, "masters": mastersDb}
    return render(request, "handyman/pages/master_pages/mastertype.html", context=data)
