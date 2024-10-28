"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from emissary_client_sdk.types import BaseModel
from emissary_client_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetEmbeddingsFromDeploymentRequestBodyTypedDict(TypedDict):
    r"""Provide your input for embeddings"""

    source_sentence: str
    r"""The input for which to get embeddings"""
    target_sentence: str
    r"""The target sentence for comparison"""
    cosine: NotRequired[bool]
    r"""Whether to return cosine similarity"""
    manhattan: NotRequired[bool]
    r"""Whether to return Manhattan distance"""
    euclidean: NotRequired[bool]
    r"""Whether to return Euclidean distance"""


class GetEmbeddingsFromDeploymentRequestBody(BaseModel):
    r"""Provide your input for embeddings"""

    source_sentence: str
    r"""The input for which to get embeddings"""

    target_sentence: str
    r"""The target sentence for comparison"""

    cosine: Optional[bool] = None
    r"""Whether to return cosine similarity"""

    manhattan: Optional[bool] = None
    r"""Whether to return Manhattan distance"""

    euclidean: Optional[bool] = None
    r"""Whether to return Euclidean distance"""


class GetEmbeddingsFromDeploymentRequestTypedDict(TypedDict):
    project_id: str
    r"""The ID of the project to retrieve deployments for"""
    deployment_id: str
    r"""The ID of the deployment to get embeddings from"""
    request_body: GetEmbeddingsFromDeploymentRequestBodyTypedDict
    r"""Provide your input for embeddings"""


class GetEmbeddingsFromDeploymentRequest(BaseModel):
    project_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the project to retrieve deployments for"""

    deployment_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the deployment to get embeddings from"""

    request_body: Annotated[
        GetEmbeddingsFromDeploymentRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Provide your input for embeddings"""


class EmbeddingsTypedDict(TypedDict):
    text1: NotRequired[List[float]]
    r"""The embedding vector for the source sentence"""
    text2: NotRequired[List[float]]
    r"""The embedding vector for the target sentence"""


class Embeddings(BaseModel):
    text1: Optional[List[float]] = None
    r"""The embedding vector for the source sentence"""

    text2: Optional[List[float]] = None
    r"""The embedding vector for the target sentence"""


class ResponseTypedDict(TypedDict):
    embeddings: NotRequired[EmbeddingsTypedDict]
    cosine_score: NotRequired[float]
    r"""The cosine similarity between the embeddings if cosine = true"""
    manhattan_distance: NotRequired[float]
    r"""The Manhattan distance between the embeddings if manhattan = true"""
    euclidean_distance: NotRequired[float]
    r"""The Euclidean distance between the embeddings if euclidean = true"""


class Response(BaseModel):
    embeddings: Optional[Embeddings] = None

    cosine_score: Optional[float] = None
    r"""The cosine similarity between the embeddings if cosine = true"""

    manhattan_distance: Optional[float] = None
    r"""The Manhattan distance between the embeddings if manhattan = true"""

    euclidean_distance: Optional[float] = None
    r"""The Euclidean distance between the embeddings if euclidean = true"""


class GetEmbeddingsFromDeploymentResponseBodyTypedDict(TypedDict):
    r"""Successful operation"""

    id: NotRequired[str]
    r"""The unique identifier for the embedding"""
    response: NotRequired[ResponseTypedDict]


class GetEmbeddingsFromDeploymentResponseBody(BaseModel):
    r"""Successful operation"""

    id: Optional[str] = None
    r"""The unique identifier for the embedding"""

    response: Optional[Response] = None
