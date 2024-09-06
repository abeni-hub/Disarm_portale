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
from rest_framework import viewsets
from .serializers import MediaSerializer
from rest_framework.response import Response
from .models import Media
class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


def get_serializer(self, *args, **kwargs):
    serializer = super().get_serializer(*args, **kwargs)
    if self.request.method in ['GET', 'POST', 'PUT']:
        # Get the media type from the request data or instance
        media_type = self.request.data.get('media_type') if self.request.data else None

        if media_type == 'video':
            # Include only video-specific fields
            serializer.fields.pop('pdf_file', None)
            serializer.fields.pop('pdf_summary', None)
            serializer.fields.pop('pdf_url', None)
            serializer.fields.pop('image_file', None)
        elif media_type == 'pdf':
            # Include only PDF-specific fields
            serializer.fields.pop('video_file', None)
            serializer.fields.pop('video_url', None)
            serializer.fields.pop('video_source', None)
            serializer.fields.pop('image_file', None)
        elif media_type == 'image':
            # Include only image-specific fields
            serializer.fields.pop('video_file', None)
            serializer.fields.pop('video_url', None)
            serializer.fields.pop('video_source', None)
            serializer.fields.pop('pdf_file', None)
            serializer.fields.pop('pdf_summary', None)
            serializer.fields.pop('pdf_url', None)

    return serializer
