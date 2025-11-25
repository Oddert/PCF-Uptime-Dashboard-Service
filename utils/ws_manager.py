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
        pcf_guid = instance.pcf_guid
        if pcf_guid in self.instances:
            for listener in self.instances[pcf_guid]:
                await listener.send_json(instance.to_json())


ws_manager = WSManager()
