
from channels.routing import route
from .consumers import websocket_receive,websocket_connect

channel_routing = [
    route("websocket.receive", websocket_receive, path=r"^/chat/"),
    # route("websocket.connect", websocket_connect, path=r"^/chat/"),
]