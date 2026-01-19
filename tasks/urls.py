from django.urls import path
from .views import TaskCreateListView

urlpatterns = [
    path('', TaskCreateListView.as_view(), name='task-list-create'),
]
