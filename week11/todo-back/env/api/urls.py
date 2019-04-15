from django.urls import path
from api import views


urlpatterns=[
    path('api/task_lists/', views.lists),
    path('api/task_lists/<int:pk>/',views.task_list_detail),
    path('api/task_lists/<int:pk>/tasks/',views.list_tasks),
]