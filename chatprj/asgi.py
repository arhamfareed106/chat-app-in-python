"""
ASGI config for chatprj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

from email.mime import application
import os
from channels.routing import ProtocolTypeRouter, URLRouter 
from chatapp import routing
import channels
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatprj.settings')

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket":URLRouter(
        routing.websocket_urlpatterns
    )
})

