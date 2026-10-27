
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
from inventory.views import ProductViewSet
router.register("products", ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('api/', include(router.urls)),


]
