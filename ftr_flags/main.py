from ftr_flags.manager import FeatureFlagManager
from ftr_flags.api import create_app


ftr_mgr = FeatureFlagManager(ftr_cfg_path='ftr_flags/config.yaml')
app = create_app(ftr_mgr)

#
#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="0.0.0.0", port=8000)