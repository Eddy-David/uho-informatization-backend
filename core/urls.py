from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import StatusAPIView, DashboardAPIView

urlpatterns = [
    path('status/', StatusAPIView.as_view(), name='status'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
