from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Text(BaseModel):
    content: Optional[str] = None
    beginOffset: Optional[int] = None


class Sentiment(BaseModel):
    magnitude: Optional[float] = None
    score: Optional[float] = None


class Sentence(BaseModel):
    text: Optional[Text] = None
    sentiment: Optional[Sentiment] = None


class Text1(BaseModel):
    content: Optional[str] = None
    beginOffset: Optional[int] = None


class Mention(BaseModel):
    text: Optional[Text1] = None
    type: Optional[str] = None


class Entity(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    salience: Optional[float] = None
    mentions: Optional[List[Mention]] = None


class DocumentSentiment(BaseModel):
    magnitude: Optional[float] = None
    score: Optional[float] = None


class Model(BaseModel):
    sentences: Optional[List[Sentence]] = None
    tokens: Optional[List] = None
    entities: Optional[List[Entity]] = None
    documentSentiment: Optional[DocumentSentiment] = None
    language: Optional[str] = None
    categories: Optional[List] = None
    fileName: Optional[str] = None
    PetID: Optional[str] = None
