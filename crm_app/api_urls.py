from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)  # Handles API for customers

urlpatterns = router.urls
