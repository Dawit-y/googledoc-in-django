import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('type') == 'update_content':
            # Process the received content data if needed
            content = data.get('content')
            # Echo back the received content to all connected clients
            print(content)
            await self.channel_layer.group_send(
                'editor_updates',
                {
                    'type': 'send_content',
                    'content': content
                }
            )

    async def send_content(self, event):
        content = event['content']
        await self.send(text_data=json.dumps({
            'type': 'update_content',
            'content': content
        }))
