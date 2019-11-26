import uuid

from django.db import models
from django.utils import timezone


class RoadmapParent(models.Model):
    """親ロードマップ"""
    
    class Meta:
        db_table = 'roadmap_parent'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # 投稿時に生成
    title = models.CharField(max_length=50, verbose_name='タイトル')
    overview = models.CharField(max_length=200, verbose_name='概要')
    like = models.IntegerField(verbose_name='いいね数', default=0)
    created_at = models.DateTimeField(default=timezone.now)


class Roadmap(models.Model):
    """ロードマップモデル"""
    
    class Meta:
        db_table = 'roadmap'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    detail = models.CharField(verbose_name='詳細', max_length=200, default='')
    created_at = models.DateTimeField(default=timezone.now)
    next_id = models.UUIDField(default=uuid.uuid4, editable=True, null=True)
    parent = models.ForeignKey(RoadmapParent, related_name='roadmap', verbose_name='親ロードマップ', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
