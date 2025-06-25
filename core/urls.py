from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Public API
    path('api/public/', views.public_api),

    # Protected API
    path('api/protected/', views.protected_api),

    # Register
    path('api/register/', views.register_api),

    # JWT Login & Refresh
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
