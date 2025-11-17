from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.orm import Session
from sqlalchemy.dialects.oracle import DATE, DOUBLE, INTEGER, NUMBER, NVARCHAR2, RAW
from sqlalchemy.types import BLOB, FLOAT, TEXT

from config.database import ORMBase
from config.variables import timezone

from utils.orm_utils import default_uuid


class InstanceModel(ORMBase):
    """Represents an individual PCF instance with optional information overrides."""

    __tablename__ = 'PDB_INSTANCE'

    contact_info = Column(NVARCHAR2(2000).with_variant(TEXT, 'sqlite'), nullable=True)
    instance_id = Column(
        RAW(16).with_variant(BLOB, 'sqlite'),
        default=default_uuid,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    last_updated = Column(DATE, nullable=False, default=lambda: datetime.now(timezone))
    message = Column(NVARCHAR2(1000).with_variant(TEXT, 'sqlite'), nullable=True)
    pcf_app_name = Column(NVARCHAR2(255).with_variant(TEXT, 'sqlite'), nullable=False)
    pcf_cpu = Column(NUMBER().with_variant(FLOAT, 'sqlite'), nullable=True)
    pcf_guid = Column(NVARCHAR2(255).with_variant(TEXT, 'sqlite'), nullable=False)
    pcf_space = Column(NVARCHAR2(20).with_variant(TEXT, 'sqlite'), nullable=False)
    pcf_instances_total = Column(
        NUMBER().with_variant(INTEGER, 'sqlite'), nullable=False, default=1
    )
    pcf_ram = Column(NUMBER().with_variant(FLOAT, 'sqlite'), nullable=True)
    readable_name = Column(NVARCHAR2(255).with_variant(TEXT, 'sqlite'), nullable=True)
    status = Column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite'), nullable=False, default='UNKNOWN'
    )
    tick_override = Column(NUMBER().with_variant(DOUBLE, 'sqlite'), nullable=True)

    def to_json(self):
        return {
            'contactInfo': self.contact_info,
            'instanceId': self.instance_id,
            'lastUpdated': self.last_updated,
            'message': self.message,
            'pcfAppName': self.pcf_app_name,
            'pcfCpu': self.pcf_cpu,
            'pcfInstancesTotal': self.pcf_instances_total,
            'pcfRam': self.pcf_ram,
            'readableName': self.readable_name,
            'status': self.status,
            'tickOverride': self.tick_override,
        }

    @classmethod
    def find_by_app_id(cls, instance_id: str, database: Session):
        return database.query(cls).filter_by(instance_id=bytes.fromhex(instance_id)).first()

    @classmethod
    def find_by_pcf_guid(cls, pcf_guid: str, database: Session):
        return database.query(cls).filter_by(pcf_guid=pcf_guid).first()

    @classmethod
    def find_all(cls, database: Session):
        return database.query(cls).all()
