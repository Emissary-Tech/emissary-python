"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from emissary_client_sdk.types import BaseModel
from emissary_client_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteDatasetByIDRequestTypedDict(TypedDict):
    project_id: str
    r"""The ID of the project to retrieve datasets for"""
    dataset_id: str
    r"""The ID of the dataset to delete"""


class DeleteDatasetByIDRequest(BaseModel):
    project_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the project to retrieve datasets for"""

    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the dataset to delete"""
