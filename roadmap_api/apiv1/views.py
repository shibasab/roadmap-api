from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from roadmap.models import Roadmap
from .serializers import RoadmapSerializer


class RoadmapViewSet(viewsets.ModelViewSet):
    
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
