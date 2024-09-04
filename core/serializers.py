from rest_framework import serializers
from .models import Plan, Prepare, Execute

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class PrepareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prepare
        fields = '__all__'

class ExecuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execute
        fields = '__all__'
