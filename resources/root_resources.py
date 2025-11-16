from fastapi import APIRouter

router = APIRouter(prefix='/')

@router.get('/')
def get_root():
    return {'message': 'Hello world'}
