"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from t742874298_1.types import BaseModel
from t742874298_1.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class GetOrderByIDRequestTypedDict(TypedDict):
    order_id: int
    r"""ID of order that needs to be fetched"""


class GetOrderByIDRequest(BaseModel):
    order_id: Annotated[
        int,
        pydantic.Field(alias="orderId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of order that needs to be fetched"""