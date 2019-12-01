from django.utils.timezone import localtime
from django.test import TestCase
from rest_framework.test import APITestCase

from roadmap.models import RoadmapParent


class TestRoadmapParentView(APITestCase):
    """RoadmapParentViewのテストクラス"""
    
    TARGET_URL = '/api/v1/roadmaps/'
    
    def test_create_success(self):
        """RoadmapParentモデルの登録APIへのPOSTリクエスト"""
        
        self.maxDiff = None
        
        # APIリクエストを実行
        params = {
            "title": "aaa",
            "overview": "test",
            "roadmap": [
                {
                    "title": "teeeest",
                    "detail": "teeest",
                    "next_id": "e1e5842c-f2bb-48bf-ac67-886104783910"
                },
                {
                    "title": "teeeest",
                    "detail": "teeest",
                    "next_id": "e1e5842c-f2bb-48bf-ac67-886104783910"
                }
            ]
        }
        response = self.client.post(self.TARGET_URL, params, format='json')
        
        # データベースの状態を検証
        self.assertEqual(RoadmapParent.objects.count(), 1)
        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 201)
        roadmap_parent = RoadmapParent.objects.get()
        roadmaps = roadmap_parent.roadmap.all()
        expected_json_dict = {
            'id': str(roadmap_parent.id),
            'title': roadmap_parent.title,
            'overview': roadmap_parent.overview,
            'like': 0,
            'created_at': str(localtime(roadmap_parent.created_at)).replace(' ', 'T'),
            'roadmap': [{
                'id': str(roadmaps[i].id),
                'title': roadmaps[i].title,
                'detail': roadmaps[i].detail,
                'next_id': str(roadmaps[i].next_id)
            } for i in range(len(roadmaps))]
        }
        self.assertJSONEqual(response.content, expected_json_dict)
