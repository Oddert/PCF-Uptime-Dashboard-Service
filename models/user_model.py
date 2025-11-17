from datetime import datetime
from typing import List

from sqlalchemy import Column
from sqlalchemy.orm import Session
from sqlalchemy.dialects.oracle import DATE, NVARCHAR2, RAW
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.types import BLOB, TEXT

from config.database import ORMBase
from config.variables import timezone

from utils.orm_utils import default_uuid


class UserModel(ORMBase):
    """Represents a system user."""

    __tablename__ = 'PDB_USER'

    areas = Column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=False,
        default='',
    )
    created_on = Column(DATE, nullable=False, default=lambda: datetime.now(timezone))
    password = Column(
        NVARCHAR2(100).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    readable_name = Column(
        NVARCHAR2(100).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    user_id = Column(
        RAW(16).with_variant(BLOB, 'sqlite').with_variant(BYTEA, 'postgresql'),
        default=default_uuid,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    username = Column(
        NVARCHAR2(100).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )

    def to_json(self):
        return {
            'areas': self.get_roles_as_list(),
            'createdOn': self.created_on,
            'readableName': self.readable_name,
            'userId': self.user_id,
            'username': self.username,
        }

    def get_roles_as_list(self) -> List[str]:
        return self.areas.split(',')

    @classmethod
    def find_by_username(cls, username: str, database: Session):
        return database.query(cls).filter_by(username=username).first()
