from django.urls import path
from .views import (
    UserPostsListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('', UserPostsListView.as_view(), name='notes-home'),
    path('note/<int:pk>/', PostDetailView.as_view(), name='note-detail'),
    path('note/new/', PostCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update/', PostUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', PostDeleteView.as_view(), name='note-delete'),
]