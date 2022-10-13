from django.urls import path
from .import views


urlpatterns= [
    path('', views.Home.as_view(), name='home'),
    path('boards/', views.BoardList.as_view(), name='board_list'),
    path('boards/new', views.BoardCreate.as_view(), name='board_create'),
    path('boards/<int:pk>/', views.BoardDetail.as_view(), name='board_detail'),
    path('boards/<int:pk>/update', views.BoardUpdate.as_view(), name='board_update'),
    path('boards/<int:pk>/delete', views.BoardDelete.as_view(), name='board_delete'),
    path('boards/<int:pk>/gifts/new/', views.Gift_IdeaCreate.as_view(), name='gift_create'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]