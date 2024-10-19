from django.shortcuts import render


mastersDb = [
    {
        "id": 1,
        "name": "Mastert1",
        "number": "111",
        "skill": "sdf",
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
        "skill": "sdf",
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
        "skill": "sdf",
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
        "skill": "sdf",
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
        "skill": "sdf",
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
        "skill": "sdf",
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
    return render(request, "handyman/pages/about.html", context=data)


def contacts(request):
    data = {"title": "Контакты"}
    return render(request, "handyman/pages/contacts.html", context=data)


def masters(request):
    data = {"title": "Мастера"}
    return render(request, "handyman/pages/masters.html", context=data)
