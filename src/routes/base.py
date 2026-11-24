from fastapi import FastAPI , APIRouter,Depends
from helpers.config import get_settings, Settings



base_router = APIRouter(
    prefix="/api/v1",
    tags=["api/v1"],
)

@base_router.get("/welcome")
def welcome(app_settings : Settings =Depends(get_settings)):


    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "message":"Hello World this app is name ",
        "app_name":app_name,
        "app_version":app_version,
    }
