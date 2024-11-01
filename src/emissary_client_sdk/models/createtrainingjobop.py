"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from emissary_client_sdk.types import BaseModel
from emissary_client_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


ParametersTypedDict = Union[str, float, int]


Parameters = Union[str, float, int]


class CreateTrainingJobRequestBodyTypedDict(TypedDict):
    r"""Provide your training job details"""

    base_model: str
    r"""The base model to fine-tune. To see full list of supported base model please visit [Base Models](https://docs.withemissary.com/models)"""
    train_dataset_id: str
    r"""The dataset ID to use for training"""
    test_dataset_id: NotRequired[str]
    r"""The test dataset ID to use for validation"""
    train_test_split_ratio: NotRequired[float]
    r"""The ratio of training to testing data"""
    name: NotRequired[str]
    r"""The name of the training job"""
    description: NotRequired[str]
    r"""A description of the training job"""
    parameters: NotRequired[Dict[str, ParametersTypedDict]]
    r"""Additional parameters for the training job"""
    hf_model_link: NotRequired[str]
    r"""Link to the Hugging Face model / Use only when you use the HF_MODEL as a base"""


class CreateTrainingJobRequestBody(BaseModel):
    r"""Provide your training job details"""

    base_model: str
    r"""The base model to fine-tune. To see full list of supported base model please visit [Base Models](https://docs.withemissary.com/models)"""

    train_dataset_id: str
    r"""The dataset ID to use for training"""

    test_dataset_id: Optional[str] = None
    r"""The test dataset ID to use for validation"""

    train_test_split_ratio: Optional[float] = None
    r"""The ratio of training to testing data"""

    name: Optional[str] = None
    r"""The name of the training job"""

    description: Optional[str] = None
    r"""A description of the training job"""

    parameters: Optional[Dict[str, Parameters]] = None
    r"""Additional parameters for the training job"""

    hf_model_link: Optional[str] = None
    r"""Link to the Hugging Face model / Use only when you use the HF_MODEL as a base"""


class CreateTrainingJobRequestTypedDict(TypedDict):
    project_id: str
    r"""The ID of the project to create a training job for"""
    request_body: CreateTrainingJobRequestBodyTypedDict
    r"""Provide your training job details"""


class CreateTrainingJobRequest(BaseModel):
    project_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the project to create a training job for"""

    request_body: Annotated[
        CreateTrainingJobRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Provide your training job details"""
