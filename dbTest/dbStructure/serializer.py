from rest_framework.serializers import ModelSerializer

from dbStructure.models import Worker, Lead_Department, Director


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class LeadSerializer(ModelSerializer):
    class Meta:
        model = Lead_Department
        fields = '__all__'

class DirSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
