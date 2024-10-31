"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from emissary_client_sdk.types import BaseModel
from emissary_client_sdk.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DeleteDeploymentByIDGlobalsTypedDict(TypedDict):
    project_id: NotRequired[str]


class DeleteDeploymentByIDGlobals(BaseModel):
    project_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class DeleteDeploymentByIDRequestTypedDict(TypedDict):
    deployment_id: str
    r"""The ID of the deployment to delete"""
    project_id: NotRequired[str]


class DeleteDeploymentByIDRequest(BaseModel):
    deployment_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the deployment to delete"""

    project_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
