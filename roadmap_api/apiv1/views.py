from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from roadmap.models import Roadmap
from .serializers import RoadmapSerializer


class RoadmapListCreate(APIView):
    
    def get(self, request, format=None):
        roadmap = Roadmap.objects.all()
        serializer = RoadmapSerializer(roadmap, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RoadmapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
class RoadmapDetails(APIView):
    
    def get_object(self, pk):
        try:
            return Roadmap.objects.get(pk=pk)
        except Roadmap.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        roadmap = self.get_object(pk)
        serializer = RoadmapSerializer(roadmap)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        roadmap = self.get_object(pk)
        serializer = RoadmapSerializer(roadmap, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        roadmap = self.get_object(pk)
        roadmap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
