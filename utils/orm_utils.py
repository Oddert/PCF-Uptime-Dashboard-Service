from uuid import uuid4 as uuid

from sqlalchemy import text
from sqlalchemy.engine.default import DefaultExecutionContext

def default_uuid(context: DefaultExecutionContext):
    '''
    Function to be used exclusively in Column 'default' attributes.
    Returns a `sys_guid` call for Oracle-like systems but returns a more generic UUID for SQLite.
    '''
    if context.engine.dialect == 'sqlite':
        return uuid().bytes
    return text('SYS_GUID()')
