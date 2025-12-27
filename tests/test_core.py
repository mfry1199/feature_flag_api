from ftr_flags.core import FeatureFlag
import yaml



def test_ftrflag():
    config_yaml = """
        enabled: true
        context:
            environments:
                prod:
                    rollout: 0
                dev:
                    rollout: 100
                staging:
                    rollout: 100
        """
    test_config = yaml.safe_load(config_yaml)

    ftr_flag = FeatureFlag('test-feature', test_config)
    
    test_context = {"environments": {"prod": {"rollout": 0},
                    "dev": {"rollout": 100},
                    "staging": {"rollout": 100}}}
    
    assert ftr_flag.decision() == (True, test_context)