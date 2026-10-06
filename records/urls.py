from rest_framework.routers import DefaultRouter
from .views import MedicalRecordViewSet

router = DefaultRouter()
router.register(r'records', MedicalRecordViewSet)

urlpatterns = router.urls