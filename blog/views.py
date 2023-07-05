from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Post, Like
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

def get_client_ip(request):
    """Получение ip-адреса клиента сайта"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.splt(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    """Добавление лайков к отдельной записи"""
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Like.objects.get(ip=ip_client, post_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Like()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DisLike(View):
    """Удаление лайков с определенной записи"""
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Like.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')