# Маршрутизация для приложения blog

from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.PostView.as_view()),
    # Страница конкретной записи
    path('<int:pk>/', views.PostDetail.as_view()),
    # Добавление нового комментария к записи
    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
]