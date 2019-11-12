from django.contrib import admin

from .models import Roadmap


class RoadmapModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'id', 'next_id', 'created_at')
    ordering = ('-created_at', )
    readonly_fields = ('id', 'created_at')

    
admin.site.register(Roadmap, RoadmapModelAdmin)
