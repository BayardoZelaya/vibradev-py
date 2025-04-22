import uuid
from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, Request

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.limiter import limiter

#

