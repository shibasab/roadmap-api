from rest_framework import serializers

from roadmap.models import Roadmap, RoadmapParent
from drf_writable_nested.serializers import WritableNestedModelSerializer


class RoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roadmap
        fields = ['id', 'title', 'detail', 'next_id']
        extra_kwargs = {
            'id': {
                'read_only': True,
            }
        }


class RoadmapParentSerializer(WritableNestedModelSerializer):
    roadmap = RoadmapSerializer(many=True)
    
    class Meta:
        model = RoadmapParent
        fields = ['id', 'title', 'overview', 'like', 'created_at', 'roadmap']
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'created_at': {
                'read_only': True,
            }
        }
        
    def create(self, validated_data):
        roadmap_data = validated_data.pop('roadmap')
        roadmap_parent = RoadmapParent.objects.create(**validated_data)
        for roadmap in roadmap_data:
            Roadmap.objects.create(parent=roadmap_parent, **roadmap)
        return roadmap_parent


class RoadmapParentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapParent
        fields = ['id', 'title', 'overview', 'like', 'created_at']
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'created_at': {
                'read_only': True,
            }
        }
