from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, PrepareViewSet, ExecuteViewSet

# Create a router and register the viewsets with it
router = DefaultRouter()
router.register(r'plans', PlanViewSet)      # Registers /api/plans/ endpoint
router.register(r'prepares', PrepareViewSet) # Registers /api/prepares/ endpoint
router.register(r'executes', ExecuteViewSet) # Registers /api/executes/ endpoint

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  # Includes all registered routes
]
