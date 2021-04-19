from django.urls import path, include
from .views import usersView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', usersView, basename="user")

urlpatterns = [
    # path('home/', home),
]

urlpatterns += router.urls