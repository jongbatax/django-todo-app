from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_home, name="todo_home"),
    path("update-status", views.update_status, name="update_status"),
    path("delete-todo", views.delete_todo, name="delete_todo"),
    path("edit-todo/<int:id>", views.edit_todo, name="edit_todo"),
    path("update-todo", views.update_todo, name="update_todo"),
]
