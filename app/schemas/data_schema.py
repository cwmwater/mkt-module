from pydantic import BaseModel, Field
from typing import List

class ContentKeywordsInput(BaseModel):
    product_info: str = Field(..., alias="productInfo")
    product_features: str = Field(..., alias="productFeatures")
    user_experience: str = Field(..., alias="userExperience")

    class Config:
        allow_population_by_field_name = True  # 내부에서 field_name으로도 접근 가능

class ToneExample(BaseModel):
    text: str
    embedding: List[float]

class ContentInput(BaseModel):
    product_info: str = Field(..., alias="productInfo")
    product_features: str = Field(..., alias="productFeatures")
    user_experience: str = Field(..., alias="userExperience")
    selected_tone: str = Field(..., alias="selectedTone")
    tone_preview: str = Field(..., alias="tonePreview")  # 예문이 하나도 없을 때의 폴백
    tone_examples: List[ToneExample] = Field(default_factory=list, alias="toneExamples")  # RAG 검색 대상
    keywords: str = Field(..., alias="keywords")

    class Config:
        allow_population_by_field_name = True  # 내부에서 snake_case로 접근 가능

class TitleKeywordsInput(BaseModel):
    generated_content: str = Field(..., alias="generatedContent")

    class Config:
        allow_population_by_field_name = True  # 내부에서 field_name으로도 접근 가능

class TitleInput(BaseModel):
    keywords: str = Field(..., alias="keywords")
    generated_content: str = Field(..., alias="generatedContent")

    class Config:
        validate_by_name = True  # v2 대응
        # alias 사용 가능, 내부에서는 generated_content 로 접근 가능

class EmbedInput(BaseModel):
    text: str = Field(..., alias="text")

    class Config:
        allow_population_by_field_name = True