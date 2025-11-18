from datetime import datetime

from sqlalchemy.dialects.postgresql import BYTEA, DOUBLE_PRECISION
from sqlalchemy.dialects.oracle import DATE, NUMBER, NVARCHAR2, RAW
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy.types import BLOB, DOUBLE, INTEGER, FLOAT, TEXT

from config.database import ORMBase
from config.variables import timezone

from utils.orm_utils import default_uuid


class InstanceModel(ORMBase):
    """Represents an individual PCF instance with optional information overrides."""

    __tablename__ = 'PDB_INSTANCE'

    contact_info: Mapped[str] = mapped_column(
        NVARCHAR2(2000).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )
    instance_id: Mapped[bytes] = mapped_column(
        RAW(16).with_variant(BLOB, 'sqlite').with_variant(BYTEA, 'postgresql'),
        default=default_uuid,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    last_updated: Mapped[datetime] = mapped_column(
        DATE, nullable=False, default=lambda: datetime.now(timezone)
    )
    message: Mapped[str] = mapped_column(
        NVARCHAR2(1000).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )
    pcf_app_name: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    pcf_cpu: Mapped[float] = mapped_column(
        NUMBER().with_variant(FLOAT, 'sqlite', 'postgresql'), nullable=True
    )
    pcf_guid: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    pcf_space: Mapped[str] = mapped_column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    pcf_instances_total: Mapped[int] = mapped_column(
        NUMBER().with_variant(INTEGER, 'sqlite', 'postgresql'),
        nullable=False,
        default=1,
    )
    pcf_ram: Mapped[float] = mapped_column(
        NUMBER().with_variant(FLOAT, 'sqlite', 'postgresql'), nullable=True
    )
    readable_name: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )
    status: Mapped[str] = mapped_column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=False,
        default='UNKNOWN',
    )
    tick_override: Mapped[float] = mapped_column(
        NUMBER()
        .with_variant(DOUBLE, 'sqlite')
        .with_variant(DOUBLE_PRECISION, 'postgresql'),
        nullable=True,
    )

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
        return (
            database.query(cls)
            .filter_by(instance_id=bytes.fromhex(instance_id))
            .first()
        )

    @classmethod
    def find_by_pcf_guid(cls, pcf_guid: str, database: Session):
        return database.query(cls).filter_by(pcf_guid=pcf_guid).first()

    @classmethod
    def find_all(cls, database: Session):
        return database.query(cls).all()
