from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from roadmap.models import Roadmap, RoadmapParent
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from .serializers import RoadmapSerializer, RoadmapParentSerializer, RoadmapParentListSerializer


class RoadmapParentView(APIView):
    @extend_schema(
        tags=["roadmaps"],
        request=RoadmapParentSerializer,
        responses={
            200: RoadmapParentListSerializer(many=True),
            201: RoadmapParentSerializer,
            400: OpenApiResponse(description="Validation error"),
        },
        summary="ロードマップ親の一覧取得・作成",
        description="GETでロードマップ親一覧、POSTで親+子ロードマップを作成します。",
    )
    
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
    @extend_schema(
        tags=["roadmaps"],
        parameters=[
            OpenApiParameter("pk", str, description="親ロードマップUUID"),
        ],
        responses={
            200: RoadmapParentSerializer,
            204: OpenApiResponse(description="Deleted"),
            404: OpenApiResponse(description="Not Found"),
        },
    )
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
    
    @extend_schema(
        tags=["roadmaps"],
        request=RoadmapParentSerializer,
        parameters=[OpenApiParameter("pk", str, description="親ロードマップUUID")],
        responses={200: RoadmapParentSerializer, 400: OpenApiResponse(description="Validation error")} ,
    )
    def put(self, request, pk, format=None):
        """roadmapのidを必ず指定する"""
        roadmap = self.get_object(pk)
        serializer = RoadmapParentSerializer(roadmap, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=["roadmaps"],
        parameters=[OpenApiParameter("pk", str, description="親ロードマップUUID")],
        responses={204: OpenApiResponse(description="Deleted")},
    )
    def delete(self, request, pk, format=None):
        roadmap = self.get_object(pk)
        roadmap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
