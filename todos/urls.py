from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_todos, name="get_todos"),
    path("<int:id>", views.get_todo, name="get_todo"),
    path("create", views.post_todo, name="post_todo"),
    path("update/<int:id>", views.put_todo, name="put_todo"),
    path("delete/<int:id>", views.delete_todo, name="delete_todo"),
]