"""Handles all responses on the base endpoint "/"."""
from typing import List

from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from config.database import get_db

from constants.auth_constants import auth_areas

from models.instance_model import InstanceModel

from mocks.fake_pcf_api import fake_pcf_call

from security.middleware import protected_endpoint

from utils.responses import respond_not_found, respond_ok, respond_server_error

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
        instances = InstanceModel.find_all(database)
        return respond_ok(
            response, instances=[instance.to_json() for instance in instances]
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/app-id/{instance_id}')
@protected_endpoint()
def get_single_instance_by_id(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a specific instance by ID. Note that this is the app's internal ID not the PCF GUD."""

    try:
        instance = InstanceModel.find_by_app_id(instance_id, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for ID "{instance_id}".'
            )

        return respond_ok(response, instance=instance.to_json())
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/pcf-id/{instance_id}')
@protected_endpoint()
def get_single_instance_by_pcf_guid(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a specific instance by ID. Note that this is the PCF GUD the app's internal ID."""

    try:
        instance = InstanceModel.find_by_pcf_guid(instance_id, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for PCF ID "{instance_id}".'
            )

        return respond_ok(response, instance=instance.to_json())
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/')
@protected_endpoint(for_areas=[auth_areas.ADMIN])
def syc_and_create_instances(
    request: Request, response: Response, database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Checks all PCF spaces to create or delete instances based on the current makeup of PCF."""

    try:
        for pcf_org in fake_pcf_call:
            for pcf_instance in pcf_org['instances']:
                queried_app_instance = InstanceModel.find_by_pcf_guid(
                    pcf_instance['guid'], database
                )
                if not queried_app_instance:
                    queried_app_instance = InstanceModel(
                        pcf_app_name=pcf_instance['name'],
                        pcf_cpu=0,
                        pcf_guid=pcf_instance['guid'],
                        pcf_space='',
                        pcf_instances_total=1,
                        pcf_ram=1,
                        readable_name=pcf_instance['name'],
                    )
                    database.add(queried_app_instance)

        database.commit()
        return respond_ok(
            response, message='Instance list created and synced with PCF.'
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))
