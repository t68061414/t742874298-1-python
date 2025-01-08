"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from t742874298_1.types import BaseModel
from t742874298_1.utils import FieldMetadata, SecurityMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SecurityTypedDict(TypedDict):
    api_key: NotRequired[str]


class Security(BaseModel):
    api_key: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="apiKey",
                sub_type="header",
                field_name="api_key",
            )
        ),
    ] = None
