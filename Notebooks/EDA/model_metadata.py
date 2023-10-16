from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class LabelAnnotation(BaseModel):
    mid: Optional[str] = None
    description: Optional[str] = None
    score: Optional[float] = None
    topicality: Optional[float] = None


class Color1(BaseModel):
    red: Optional[int] = None
    green: Optional[int] = None
    blue: Optional[int] = None


class Color(BaseModel):
    color: Optional[Color1] = None
    score: Optional[float] = None
    pixelFraction: Optional[float] = None


class DominantColors(BaseModel):
    colors: Optional[List[Color]] = None


class ImagePropertiesAnnotation(BaseModel):
    dominantColors: Optional[DominantColors] = None


class Vertice(BaseModel):
    x: Optional[int] = None
    y: Optional[int] = None


class BoundingPoly(BaseModel):
    vertices: Optional[List[Vertice]] = None


class CropHint(BaseModel):
    boundingPoly: Optional[BoundingPoly] = None
    confidence: Optional[float] = None
    importanceFraction: Optional[float] = None


class CropHintsAnnotation(BaseModel):
    cropHints: Optional[List[CropHint]] = None


class Model(BaseModel):
    labelAnnotations: Optional[List[LabelAnnotation]] = None
    imagePropertiesAnnotation: Optional[ImagePropertiesAnnotation] = None
    cropHintsAnnotation: Optional[CropHintsAnnotation] = None
    fileName: Optional[str] = None
    PetID: Optional[str] = None
