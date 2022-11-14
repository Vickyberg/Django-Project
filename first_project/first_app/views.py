from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

todos = {
    "monday": "<h1>Attend fellowship meeting<h1/>   ",
    "tuesday": "<h1>See Susan<h1/>"
}


# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Django</h1>")


def todo(request, day):
    try:
        return HttpResponse(todos[day])
    except KeyError:
        return HttpResponse("<h1>Day Not Found<h1/>")


def todo_by_number(request, number):
    day_list = list(todos.keys())
    day_todo = day_list[number - 1]
    return HttpResponseRedirect(f"/myapp/{day_todo}")
