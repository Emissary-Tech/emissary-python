"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from emissary_client_sdk.types import BaseModel
from emissary_client_sdk.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListDatasetsGlobalsTypedDict(TypedDict):
    project_id: NotRequired[str]


class ListDatasetsGlobals(BaseModel):
    project_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class ListDatasetsRequestTypedDict(TypedDict):
    project_id: NotRequired[str]


class ListDatasetsRequest(BaseModel):
    project_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
