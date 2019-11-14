import uuid

from django.db import models
from django.utils import timezone


class Roadmap(models.Model):
    """ロードマップモデル"""
    
    class Meta:
        db_table = 'roadmap'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    detail = models.CharField(verbose_name='詳細', max_length=200, default='')
    created_at = models.DateTimeField(default=timezone.now)
    next_id = models.UUIDField(default=uuid.uuid4, editable=True, null=True)
    
    def __str__(self):
        return self.title
