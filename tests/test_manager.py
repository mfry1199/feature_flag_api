import pytest
from ftr_flags.manager import FeatureFlagManager

@pytest.mark.unit
def test_feature_flag_manager(tmp_path):
    yaml_content = """
        feature-flags:
            centerline-artifacts:
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
    
    yaml_file = tmp_path / "flag.yaml"
    yaml_file.write_text(yaml_content)

    ftr_manager = FeatureFlagManager(yaml_file)

    ftr_flag_eval = ftr_manager.eval_ftr_flag({"feature": "centerline-artifacts"})

    assert ftr_flag_eval == {"feature_name":"centerline-artifacts",
                            "flag": True,
                            "context": 
                            {"environments": 
                            {"prod": {"rollout": 0},
                            "dev": {"rollout": 100},
                            "staging": {"rollout": 100}}}}
   

    