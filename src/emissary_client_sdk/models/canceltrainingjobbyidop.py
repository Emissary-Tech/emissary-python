"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from emissary_client_sdk.types import BaseModel
from emissary_client_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class CancelTrainingJobByIDRequestTypedDict(TypedDict):
    project_id: str
    r"""The ID of the project to retrieve training jobs for"""
    training_job_id: str
    r"""The ID of the training job to cancel"""


class CancelTrainingJobByIDRequest(BaseModel):
    project_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the project to retrieve training jobs for"""

    training_job_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the training job to cancel"""
