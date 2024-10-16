from django.shortcuts import render


def index(request):
    data = {"title": "HandyMan"}
    return render(request, "handyman/index.html", context=data)


def about(request):
    data = {"title": "about"}
    return render(request, "handyman/about.html", context=data)
