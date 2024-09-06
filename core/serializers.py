from rest_framework import serializers
from .models import Plan, Prepare, Execute
from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    strategy_text = serializers.SerializerMethodField()
    objective_text = serializers.SerializerMethodField()
    target_audience_text = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['strategy', 'strategy_text', 'objective', 'objective_text', 'target_audience_analysis', 'target_audience_text']

    def get_strategy_text(self, obj):
        # Map strategy to its relevant additional details key
        choices_to_text = {
            'Determine Target Audience': 'determine_target_audience',
            'Determine Target Ends': 'determine_target_ends',
        }
        strategy_key = choices_to_text.get(obj.strategy)
        if obj.additional_details and strategy_key:
            return obj.additional_details.get(strategy_key, '')
        return ''

    def get_objective_text(self, obj):
        # Map objective to its relevant additional details key
        choices_to_text = {
            'Degrade Adversary': 'degrade_adversary',
            'Discredit Credible Sources': 'discredit_sources',
            'Distract': 'distract',
            'Dismiss': 'dismiss',
            'Divide': 'divide',
        }
        objective_key = choices_to_text.get(obj.objective)
        if obj.additional_details and objective_key:
            return obj.additional_details.get(objective_key, '')
        return ''

    def get_target_audience_text(self, obj):
        # Map target audience analysis to its relevant additional details key
        choices_to_text = {
            'Identify Target Audience Adversaries': 'identify_adversaries',
            'Identify Wedge Issues': 'identify_wedge_issues',
            'Find Echo Chambers': 'find_echo_chambers',
            'Identify Data Voids': 'identify_data_voids',
        }
        target_audience_key = choices_to_text.get(obj.target_audience_analysis)
        if obj.additional_details and target_audience_key:
            return obj.additional_details.get(target_audience_key, '')
        return ''

class PrepareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prepare
        fields = '__all__'

class ExecuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execute
        fields = '__all__'
from rest_framework import serializers
from .models import Media

class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'

    # def to_representation(self, instance):
    #     # Overriding to represent only relevant fields
    #     representation = super().to_representation(instance)
    #     media_type = instance.media_type
    #
    #     if media_type == 'video':
    #         # Keep only video-related fields
    #         allowed_fields = ['title', 'media_type', 'description', 'video_file', 'video_url', 'video_source', 'created_at', 'updated_at']
    #     elif media_type == 'pdf':
    #         # Keep only PDF-related fields
    #         allowed_fields = ['title', 'media_type', 'description', 'pdf_file', 'pdf_summary', 'pdf_url', 'created_at', 'updated_at']
    #     elif media_type == 'image':
    #         # Keep only image-related fields
    #         allowed_fields = ['title', 'media_type', 'description', 'image_file', 'created_at', 'updated_at']
    #     else:
    #         # In case of other types, default to all fields
    #         allowed_fields = ['title', 'media_type', 'description', 'created_at', 'updated_at']
    #
    #     # Remove unwanted fields
    #     return {key: value for key, value in representation.items() if key in allowed_fields}