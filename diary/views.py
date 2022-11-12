from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Note
from django.contrib import messages


class UserPostsListView(ListView):
    model = Note
    template_name = 'diary/home_page.html'
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.is_valid():
            messages.success(self.request, message=f'Запись создана.')
        else:
            messages.error(self.request, message="Не удалось создать запись.")
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/diary/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False






