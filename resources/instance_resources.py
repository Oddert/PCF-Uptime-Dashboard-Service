"""Handles all responses on the base endpoint "/instance"."""

from datetime import datetime
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
)
from loguru import logger
from sqlalchemy.orm import Session

from config.database import get_db
from config.variables import timezone

from constants.auth_constants import auth_areas

from models.instance_model import InstanceModel

from mocks.fake_pcf_api import fake_pcf_call, spaces_by_id

from security.middleware import protected_endpoint
from security.roles import get_org_ids_for_user

from utils.responses import (
    respond_not_found,
    respond_ok,
    respond_server_error,
    respond_unauthorised,
)
from utils.ws_manager import ws_manager

router = APIRouter(prefix='/instance')


@router.get('/')
@protected_endpoint()
async def get_all_instances(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all instances stored within the system."""

    try:
        org_ids = get_org_ids_for_user(roles)
        instances = InstanceModel.find_by_org_id_list(org_ids, database)
        return respond_ok(
            response, instances=[instance.to_json() for instance in instances]
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/app-id/{instance_id}')
@protected_endpoint()
async def get_single_instance_by_id(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a specific instance by ID. Note that this is the app's internal ID not the PCF GUD."""

    try:
        org_ids = get_org_ids_for_user(roles)
        instance = InstanceModel.find_by_app_id(instance_id, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for ID "{instance_id}".'
            )

        if instance.pcf_org_id not in org_ids:
            return respond_unauthorised(
                response,
                f'You do not have the required roles to access the instance with ID "{instance_id}".',
            )

        return respond_ok(response, instance=instance.to_json())
    except ValueError as ex:
        return respond_not_found(
            response,
            message=f'Instance ID of "{instance_id}" is not valid.',
            error=str(ex),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/pcf-id/{instance_id}')
@protected_endpoint()
async def get_single_instance_by_pcf_guid(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a specific instance by ID. Note that this is the PCF GUD the app's internal ID."""

    try:
        org_ids = get_org_ids_for_user(roles)
        instance = InstanceModel.find_by_pcf_guid(instance_id, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for PCF ID "{instance_id}".'
            )

        if instance.pcf_org_id not in org_ids:
            return respond_unauthorised(
                response,
                f'You do not have the required roles to access the instance with ID "{instance_id}".',
            )

        return respond_ok(response, instance=instance.to_json())
    except ValueError as ex:
        return respond_not_found(
            response,
            message=f'Instance PCF GUID of "{instance_id}" is not valid.',
            error=str(ex),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/')
@protected_endpoint(for_areas=[auth_areas.ADMIN])
async def user_sync_instances(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Endpoint to manually trigger PCF Instance syncs."""

    try:
        await syc_and_create_instances(database=database)
        return respond_ok(
            response,
            message='Instance list created and synced with PCF.',
            updated=datetime.now(timezone),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/debug')
@protected_endpoint()
async def debug_get_pcf_call(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all instances stored within the system."""

    try:
        instance_map = {}
        for organisation in fake_pcf_call:
            if organisation['org_id'] not in instance_map:
                instance_map[organisation['org_id']] = {
                    'name': organisation['org_name'],
                    'spaces': {},
                }

            for instance in organisation['instances']:
                if (
                    instance['space_id']
                    not in instance_map[organisation['org_id']]['spaces']
                ):
                    instance_map[organisation['org_id']]['spaces'][
                        instance['space_id']
                    ] = {'name': spaces_by_id[instance['space_id']], 'instances': []}

                instance_map[organisation['org_id']]['spaces'][instance['space_id']][
                    'instances'
                ].append(organisation)

        return respond_ok(
            response,
            instances=instance_map,
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


async def syc_and_create_instances(
    database: Session = Depends(get_db),
):
    """Checks all PCF spaces to create or delete application Instances, based on the current makeup of PCF."""

    try:
        for pcf_org in fake_pcf_call:
            for pcf_instance in pcf_org['instances']:
                queried_app_instance = InstanceModel.find_by_pcf_guid(
                    pcf_instance['guid'], database
                )
                if queried_app_instance:
                    queried_app_instance.created_at = pcf_instance['created_at']
                    queried_app_instance.pcf_app_name = pcf_instance['name']
                    queried_app_instance.pcf_cpu = 0
                    queried_app_instance.pcf_org_id = pcf_org['org_id']
                    queried_app_instance.pcf_space_id = pcf_instance['space_id']
                    queried_app_instance.pcf_instances_total = 1
                    queried_app_instance.pcf_ram = 1
                    queried_app_instance.readable_name = pcf_instance['name']
                    queried_app_instance.updated_at = pcf_instance['updated_at']
                else:
                    queried_app_instance = InstanceModel(
                        created_at=pcf_instance['created_at'],
                        pcf_app_name=pcf_instance['name'],
                        pcf_cpu=0,
                        pcf_guid=pcf_instance['guid'],
                        pcf_org_id=pcf_org['org_id'],
                        pcf_space_id=pcf_instance['space_id'],
                        pcf_instances_total=1,
                        pcf_ram=1,
                        readable_name=pcf_instance['name'],
                        status=pcf_instance['desired_state'],
                        updated_at=pcf_instance['updated_at'],
                    )
                    database.add(queried_app_instance)
                await ws_manager.broadcast_update(queried_app_instance)

        database.commit()
        return {'message': 'Sync completed successfully'}
    except Exception as ex:
        raise ex


async def schedule_instance_sync():
    """Scheduler task to sync the Instances database."""
    try:
        logger.info('Beginning schedule of Instances from PCF')
        database = next(get_db())
        result = await syc_and_create_instances(database=database)
        logger.info('PCF sync job complete.')
        return result
    except Exception as ex:
        logger.error(str(ex))
