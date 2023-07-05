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
    # Добавление новых лайков к определенной записи
    path('<int:pk>/add_like/', views.AddLike.as_view(), name='add_like'),
    # Удаление лайков у записи
    path('<int:pk>/del_like/', views.DisLike.as_view(), name='del_like'),
]