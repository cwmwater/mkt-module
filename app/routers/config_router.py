from fastapi import APIRouter, Body, Header, HTTPException, status
from app.config.settings import settings
from app.schemas.data_schema import ModelConfigInput
from app.schemas.resp_schema import succeed
from app.services.gpt_service import get_current_model, set_current_model

router = APIRouter(prefix="/config", tags=["Admin-Config"])

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != settings.FASTAPI_API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")

# 현재 사용 중인 GPT 모델 조회 (관리자 페이지 표시용)
@router.get("/model")
async def get_model_ep():
    return succeed({"model_name": get_current_model()}).model_dump()

# 관리자용 - GPT 모델 변경 (백엔드에서 X-API-Key로 호출)
@router.put("/model")
async def update_model_ep(data: ModelConfigInput = Body(...), x_api_key: str = Header(None)):
    verify_api_key(x_api_key)
    set_current_model(data.model_name)
    return succeed({"model_name": get_current_model()}).model_dump()
