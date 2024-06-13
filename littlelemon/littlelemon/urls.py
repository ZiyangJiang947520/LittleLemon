# littlelemon/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include(router.urls)),  # 包含 BookingViewSet 的 URL 路由
    path('auth/', include('djoser.urls')),  # 添加 djoser 的 URL 路由
    path('auth/', include('djoser.urls.authtoken')),  # 添加 djoser 的 token 认证路由
]
