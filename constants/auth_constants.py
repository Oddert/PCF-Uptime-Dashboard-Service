"""Holds any application-level constant variables for the auth logic."""


class Areas:
    """
    Enum-style object to hold codes for the various valid authentication areas.
    """

    def __init__(self) -> None:
        self.STAKEHOLDER = 'STAKEHOLDER'
        self.PO = 'PO'
        self.ADMIN = 'ADMIN'


auth_areas = Areas()
