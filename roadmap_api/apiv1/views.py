from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from roadmap.models import Roadmap, RoadmapParent
from .serializers import RoadmapSerializer, RoadmapParentSerializer, RoadmapParentListSerializer


class RoadmapParentView(APIView):
    
    def get(self, request, format=None):
        """ロードマップのリストを取得"""
        roadmap_parent = RoadmapParent.objects.all()
        serializer = RoadmapParentListSerializer(roadmap_parent, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """ロードマップを投稿"""
        serializer = RoadmapParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
        
class RoadmapDetail(APIView):
    """ロードマップ全体を取得、修正、削除"""
    def get_object(self, pk):
        """parent_idがpkのものをすべて取得"""
        try:
            return RoadmapParent.objects.get(pk=pk)
        except Roadmap.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        roadmap = self.get_object(pk)
        serializer = RoadmapParentSerializer(roadmap)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        """roadmapのidを必ず指定する"""
        roadmap = self.get_object(pk)
        serializer = RoadmapParentSerializer(roadmap, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        roadmap = self.get_object(pk)
        roadmap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
