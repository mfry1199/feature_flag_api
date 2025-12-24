

class FeatureFlag:
    def __init__(self, feature_name, cfg):
        self.name = feature_name

        if cfg.get("context", None):
            self.context = EvaluationContext(cfg["context"])
        else:
            self.context = None
        
        self.enabled = cfg.get("enabled", False)
        

    def decision(context):
        pass


class FlagDecision:
    def __init__(self):
        pass


class EvaluationContext:
    def __init__(self, cxt):
        self.cxt = self.set_context(cxt)

    