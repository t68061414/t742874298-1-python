"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from t742874298_1.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CategoryTypedDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]


class Category(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None
