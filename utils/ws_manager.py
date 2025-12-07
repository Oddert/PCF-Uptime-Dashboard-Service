from typing import Dict, List

from fastapi import WebSocket

from models.instance_model import InstanceModel


class WSManager:
    def __init__(self) -> None:
        self.instances: Dict[str, List[WebSocket]] = {}

    def register_listener(self, pcf_guid: str, websocket: WebSocket):
        if pcf_guid not in self.instances:
            self.instances[pcf_guid] = []
        if websocket not in self.instances[pcf_guid]:
            self.instances[pcf_guid].append(websocket)

    def unregister_listener(self, websocket: WebSocket):
        for listener_list in self.instances.values():
            if websocket in listener_list:
                listener_list.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast_update(self, instance: InstanceModel):
        print('broadcasting: ', instance.pcf_app_name)
        pcf_guid = instance.pcf_guid
        if pcf_guid in self.instances:
            for listener in self.instances[pcf_guid]:
                await listener.send_json([instance.to_json()])

    async def broadcast_multiple_updates(self, instances: List[InstanceModel]):
        listeners: Dict[WebSocket, List[InstanceModel]] = {}
        for instance in instances:
            print('broadcasting multiple: ', instance.pcf_app_name)
            pcf_guid = instance.pcf_guid
            if pcf_guid in self.instances:
                for listener in self.instances[pcf_guid]:
                    if listener not in listeners:
                        listeners[listener] = []
                    print(f'subscribing {listener} to {instance}')
                    listeners[listener].append(instance)

        print('listeners', listeners)
        for recipient, subscriptions in listeners.items():
            await recipient.send_json([instance.to_json() for instance in subscriptions])


ws_manager = WSManager()
