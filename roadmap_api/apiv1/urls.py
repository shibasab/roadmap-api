from django.urls import path, include

from . import views


app_name = 'apiv1'
urlpatterns = [
    path('roadmaps/', views.RoadmapListCreate.as_view(), name='api-roadmap-list'),
    path('roadmaps/<uuid:pk>', views.RoadmapDetails.as_view(), name='api-roadmap-details'),
]
