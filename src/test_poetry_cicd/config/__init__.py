"""
Configuration package for AptWise backend.
"""
from .cookie_config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    COOKIE_NAME,
    EMAIL_PATTERN,
    URL_PATTERN
)

try:
    from .db_config import get_session, create_tables
except ImportError:
    # The cassandra-driver might not be installed yet
    def get_session():
        """Fallback function when cassandra is not available."""
        return None

    def create_tables():
        """Fallback function when cassandra is not available."""
        pass

__all__ = [
    "SECRET_KEY",
    "ALGORITHM",
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    "COOKIE_NAME",
    "EMAIL_PATTERN",
    "URL_PATTERN",
    "get_session",
    "create_tables"
]
