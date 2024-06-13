from django.urls import path, include
from .views import add_task, mark_as_done, mark_as_undone, edit_task, delete_task


urlpatterns = [
    path('add/', add_task, name='add_task'),
    path('mark_as_done/<int:pk>/', mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', mark_as_undone, name='mark_as_undone'),
    path('edit_task/<int:pk>/', edit_task, name="edit_task"),
    path('delete_task/<int:pk>/', delete_task, name="delete_task")



]
