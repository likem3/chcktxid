from django.urls import path
from payments.views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserSuspendView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/suspend/', UserSuspendView.as_view(), name='user-update'),
]