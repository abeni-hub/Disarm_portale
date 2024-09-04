from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Plan, Prepare, Execute
from .serializers import PlanSerializer, PrepareSerializer, ExecuteSerializer

# ViewSet for Plan
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# ViewSet for Prepare
class PrepareViewSet(viewsets.ModelViewSet):
    queryset = Prepare.objects.all()
    serializer_class = PrepareSerializer

# ViewSet for Execute
class ExecuteViewSet(viewsets.ModelViewSet):
    queryset = Execute.objects.all()
    serializer_class = ExecuteSerializer
