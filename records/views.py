
from rest_framework.viewsets import ModelViewSet
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

class MedicalRecordViewSet(ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer