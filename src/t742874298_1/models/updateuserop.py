"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .user import User, UserTypedDict
import pydantic
from t742874298_1.types import BaseModel
from t742874298_1.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateUserRequestTypedDict(TypedDict):
    username_param: str
    r"""name that needs to be updated"""
    user: NotRequired[UserTypedDict]
    r"""Update an existent user in the store"""


class UpdateUserRequest(BaseModel):
    username_param: Annotated[
        str,
        pydantic.Field(alias="username"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""name that needs to be updated"""

    user: Annotated[
        Optional[User],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Update an existent user in the store"""
