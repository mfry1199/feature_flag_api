from manager import FeatureFlagManager
from api import create_app


ftr_mgr = FeatureFlagManager(ftr_cfg_path='config.yaml')
app = create_app(ftr_mgr)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)