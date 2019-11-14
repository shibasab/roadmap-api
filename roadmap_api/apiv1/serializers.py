from rest_framework import serializers

from roadmap.models import Roadmap


class RoadmapSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Roadmap
        fields = ['id', 'title', 'detail', 'next_id']
