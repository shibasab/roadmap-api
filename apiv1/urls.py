from django.urls import path, include

from . import views


app_name = 'apiv1'
urlpatterns = [
    path('roadmaps/', views.RoadmapParentView.as_view(), name='api-roadmap-list'),
    path('roadmaps/<uuid:pk>', views.RoadmapDetail.as_view(), name='api-roadmap-details'),
]
