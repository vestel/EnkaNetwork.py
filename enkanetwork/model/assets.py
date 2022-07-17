from pydantic import BaseModel, Field
from typing import List

from ..enum import ElementType


class NamecardAsset(BaseModel):
    id: int = 0
    hash_id: str = Field("", alias="nameTextMapHash")
    icon: str = Field("", alias="icon")
    banner: str = ""
    navbar: str = ""

class CharacterIconAsset(BaseModel):
    icon: str = ""
    side: str = ""
    banner: str = ""

class CharacterSkillAsset(BaseModel):
    id: int = 0
    hash_id: str = Field("", alias="nameTextMapHash")
    icon: str = Field(None, alias="skillIcon")

class CharacterConstellationsAsset(BaseModel):
    id: int = 0
    hash_id: str = Field("", alias="nameTextMapHash")
    icon: str = Field(None, alias="icon")

class CharacterSkillAsset(BaseModel):
    id: int = 0
    hash_id: str = Field("", alias="nameTextMapHash")
    icon: str = Field(None, alias="skillIcon")

class CharacterAsset(BaseModel):
    id: int = 0
    hash_id: str = Field("", alias="nameTextMapHash")
    element: ElementType = Field(ElementType.Unknown, alias="costElemType")
    images: CharacterIconAsset = None
    skills: List[int] = []
    constellations: List[int] = Field([], alias="talents")

    class Config:
        use_enum_values = True