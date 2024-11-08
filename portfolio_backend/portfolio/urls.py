from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortflioView

router = DefaultRouter()
router.register(r"portfolio",PortflioView)

urlpatterns = [
    path('',include(router.urls)),
]