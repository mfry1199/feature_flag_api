import yaml
from core import FeatureFlag


class MissingConfigError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class MissingFeatureName(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class FeatureNotFound(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class FeatureFlagManager:
    def __init__(self, ftr_cfg_path: str):
        self.ftr_flags = self.load(ftr_cfg_path)

    def load(self, ftr_cfg_path) -> dict[str, FeatureFlag]:
        with open(self, ftr_cfg_path):
            ftr_cfg = yaml.safe_load(ftr_cfg_path)

        ftr_flag_cfg = ftr_cfg.get('feature-flags', None)
        
        if not ftr_flag_cfg:
            raise MissingConfigError("Feature flag config missing from config data.")

        ftr_flags = {}
        for ftr_flag_name, cfg in ftr_flag_cfg.items():
            ftr_flags[ftr_flag_name] = FeatureFlag(ftr_flag_name, cfg)

        return ftr_flags

    def eval_ftr_flag(self, request: dict) -> dict:
        ftr_name = request.get("feature", None)
        context = request.get("context", None)

        if not ftr_name:
            raise MissingFeatureName("The request did not succeed due to no feature name provided.")
        
        ftr = self.ftr_flags.get(ftr_name, None)

        if not ftr:
            raise FeatureNotFound(f"A feature with the name {ftr_name} has not been configured.")
        
        ftr_decision = ftr.decision(context)
        return ftr_decision