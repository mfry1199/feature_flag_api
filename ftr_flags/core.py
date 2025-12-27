class FeatureFlag:
    def __init__(self, feature_name: str, cfg: dict):
        self.name = feature_name

        if cfg.get("context", None):
            self.context = EvaluationContext(cfg["context"])
        else:
            self.context = None
        
        self.enabled = cfg.get("enabled", False)
        

    def decision(self) -> tuple[bool, dict]:
        return (self.enabled, self.context.context())


class EvaluationContext:
    def __init__(self, cxt: dict):
        self.cxt = cxt

    def context(self) -> dict:
        return self.cxt

    