from manager import FeatureManager
from fastapi import FastAPI


def create_app(ftr_mgr: FeatureManager) -> FastAPI:

    app = FastAPI()


    @app.post("/evaluate")
    async def evaluate(request: dict):
        response = ftr_mgr.eval_ftr_flag(request)
        return response


    return app