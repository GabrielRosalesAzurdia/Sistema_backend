from django.urls import path, include
from .views import usersView, CustomAuthToken
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', usersView, basename="user")

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view())
]

urlpatterns += router.urls