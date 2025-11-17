"""Handles all responses on the base endpoint "/"."""

from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from config.database import get_db

from models.instance_model import InstanceModel

from utils.responses import respond_not_found, respond_ok, respond_server_error

router = APIRouter(prefix='instance')


@router.get('/')
def get_all_instances(
    request: Request, response: Response, database: Session = Depends(get_db)
):
    """Fallback endpoint for the root of the API."""

    try:
        instances = InstanceModel.find_all(database)
        return respond_ok(
            response, instances=[instance.to_json() for instance in instances]
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/{instance_id}')
def get_single_instance(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
):
    """Fallback endpoint for the root of the API."""

    try:
        instance = InstanceModel.find_by_id(instance_id, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for ID "{instance_id}".'
            )

        return respond_ok(response, instance=instance.to_json())
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/')
def syc_and_create_instances(
    request: Request, response: Response, database: Session = Depends(get_db)
):
    """Fallback endpoint for the root of the API."""

    try:
        fake_pcf_call = []

        for pcf_instance in fake_pcf_call:
            queried_app_instance = InstanceModel.find_by_pcf_guid(pcf_instance['guid'])
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
