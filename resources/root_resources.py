"""Handles all responses on the base endpoint "/"."""

from typing import Annotated
from jwt import ExpiredSignatureError, InvalidTokenError

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
    status,
    WebSocket,
    WebSocketDisconnect,
    WebSocketException,
)
from sqlalchemy.orm import Session

from config.database import get_db

from models.instance_model import InstanceModel

from security.middleware import get_ws_token, verify_extracted_token
from security.roles import get_org_ids_for_user

from utils.exceptions import NeedsAuthorisation, NeedsLogin
from utils.responses import respond_ok
from utils.ws_manager import ws_manager

router = APIRouter()


@router.get('/')
def get_root(request: Request, response: Response):
    """Fallback endpoint for the root of the API."""
    return respond_ok(response)


@router.websocket('/ws')
async def websocket_endpoint(
    *,
    websocket: WebSocket,
    token: Annotated[str, Depends(get_ws_token)],
    database: Session = Depends(get_db),
):
    """Handles WebSocket connections, subscribing a user to receive updates from their instances."""
    try:
        await websocket.accept()
        decoded_verified_token = verify_extracted_token(token)
        org_ids = get_org_ids_for_user(decoded_verified_token['roles'])
        instances = InstanceModel.find_by_org_id_list(org_ids, database)

        for instance in instances:
            ws_manager.register_listener(instance.pcf_guid, websocket)
        try:
            while True:
                data = await websocket.receive_text()
                await ws_manager.send_personal_message(f'You wrote {data}', websocket)
        except WebSocketDisconnect:
            ws_manager.unregister_listener(websocket)
    except NeedsLogin:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except NeedsAuthorisation:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except ExpiredSignatureError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except InvalidTokenError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except ValueError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
