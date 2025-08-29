import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import lisa.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            lisa.routing.ws_urlpatterns
        )
    )
})
