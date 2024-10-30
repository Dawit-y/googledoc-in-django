from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path("ws/editor/<str:document_id>/", consumers.EditorConsumer.as_asgi()),
]