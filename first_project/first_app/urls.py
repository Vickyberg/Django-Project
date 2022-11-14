from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<str:day>/", views.todo, name="daily-todo"),
    path("<int:number>/", views.todo_by_number)

]