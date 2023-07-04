from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Post
from .form import CommentForm

class PostView(View):
    """Вывод записей на странице"""
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/post.html', {'post_list': posts})

class PostDetail(View):
    """Страница для вывода отдельной записи"""
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

class AddComment(View):
    """Добавление нового комментария к записи"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')
