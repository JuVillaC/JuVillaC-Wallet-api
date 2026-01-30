from django.urls import path
from .views import UserListView, RegisterView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='regster'),
]
