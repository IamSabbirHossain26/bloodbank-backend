from rest_framework.routers import DefaultRouter
from .views import BloodRequestViewSet

router = DefaultRouter()
router.register(r'requests', BloodRequestViewSet, basename='bloodrequest')

urlpatterns = router.urls
