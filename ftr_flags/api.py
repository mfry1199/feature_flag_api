from ftr_flags.manager import FeatureFlagManager
from fastapi import FastAPI


def create_app(ftr_mgr: FeatureFlagManager) -> FastAPI:

    app = FastAPI()


    @app.post("/evaluate")
    async def evaluate(request: dict):
        response = ftr_mgr.eval_ftr_flag(request)
        return response
    
    @app.post("/health")
    async def health():
        return 200



    return app