from django.urls import path, include
from rest_framework.routers import DefaultRouter, views
from .views import ProfileView, LoginUSer

router = DefaultRouter()
# router.register(r'profile', ProfileView, basename='profile')
# router.register(r'login', AuthenticateUSerViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]
