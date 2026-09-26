from django.urls import path
from api.users.views import ProfileAPIView, LoginAPIView, RegisterAPIView

urlpatterns = [
    path('', ProfileAPIView.as_view(), name='users-api'),
    path('register/', RegisterAPIView.as_view(), name='register-api'),
    path('login/', LoginAPIView.as_view(), name='login-api'),
]