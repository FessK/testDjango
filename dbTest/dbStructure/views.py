from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from dbStructure.models import Director, Lead_Department, Worker
from dbStructure.serializer import WorkerSerializer, LeadSerializer, DirSerializer


# Create your views here.

class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['sur_name', 'salary', 'pos_work']


class LeadViewSet(ModelViewSet):
    queryset = Lead_Department.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['sur_name', 'salary', 'pos_work']


class DirViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['second_name', 'salary', 'pos_work']
    ordering_fields = ['name', 'second_name', 'pos_work', 'pos', 'salary']
