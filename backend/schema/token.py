from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[int] = None
