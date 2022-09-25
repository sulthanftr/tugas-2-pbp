from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('selesai/<int:pk>', task_selesai, name='task-selesai'),
    path('undo/<int:pk>', undo_task, name='undo-task'),
    path('hapus/<int:pk>', hapus_task, name='hapus-task'),
]