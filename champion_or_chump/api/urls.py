from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # path('', views.getRoutes, name='routes'),
    # path('users/', views.getUsers, name='users'),
    # path('users/<str:pk>/', views.getUser, name='user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),
]