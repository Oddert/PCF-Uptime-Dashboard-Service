"""Any utility functions relating to the role based access control (RBAC) logic."""

from typing import List, Optional

from constants.auth_constants import role_lookup


class RoleValidateResult:
    """Represents the result of a role list check."""

    def __init__(self, invalid_roles: Optional[List[str]] = []) -> None:
        self.success = invalid_roles and len(invalid_roles) > 0
        self.invalid_roles = invalid_roles


def validate_role_list(roles: List[str]):
    """Checks a given list of roles against the central role list to ensure each is valid."""
    fail_list: List[str] = []
    for role in roles:
        if role not in role_lookup:
            fail_list.append(role)
    return RoleValidateResult(fail_list)
