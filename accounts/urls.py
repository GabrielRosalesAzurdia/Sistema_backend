from django.urls import path, include
from .views import usersView, MyTokenObtainPairView #CustomAuthToken
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'user', usersView, basename="user")

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh")
    #path('api-token-auth/', CustomAuthToken.as_view())
]

urlpatterns += router.urls