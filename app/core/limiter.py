"""Rate limiting for the application.

This module sets up rate limiting for the application using the `slowapi` library.
Set default rate limit to 100 requests per minute.

The rate limit can be configured using the `RATE_LIMIT` environment variable.

"""

from slowapi import Limiter
from slowapi.util import get_remote_address

import os

rate_limit = os.getenv("RATE_LIMIT", "50/minute")

limiter = Limiter(key_func=get_remote_address, default_limits=[rate_limit])