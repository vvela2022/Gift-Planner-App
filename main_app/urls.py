from django.urls import path
from .import views


urlpatterns= [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'), 
    path('boards/', views.BoardList.as_view(), name='board_list'),
    path('boards/new', views.BoardCreate.as_view(), name='board_create'),
    path('boards/<int:pk>/', views.BoardDetail.as_view(), name='board_detail')
]