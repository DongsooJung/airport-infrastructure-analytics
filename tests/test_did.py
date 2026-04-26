"""DID 추정기 테스트 스켈레톤."""
import pytest
import numpy as np
import pandas as pd

# from airport_di import DIDAnalysis
# from airport_di.data_loader import load_synthetic_panel


@pytest.fixture
def synthetic_panel():
    """treatment_effect=-0.05의 합성 패널."""
    pytest.skip("load_synthetic_panel 미구현")
    # return load_synthetic_panel(seed=42, treatment_effect=-0.05)


class TestTWFE:
    def test_recovers_known_effect(self, synthetic_panel):
        """합성 데이터에서 처리효과 -0.05를 ±0.01 오차로 추정해야 함."""
        pytest.skip("TWFE 미구현")
        # did = DIDAnalysis(synthetic_panel, outcome="outcome")
        # res = did.run_twfe()
        # assert abs(res.att - (-0.05)) < 0.01
        # assert res.p_value < 0.05

    def test_clustered_se_larger_than_iid(self, synthetic_panel):
        """Cluster SE는 일반 SE보다 보수적이어야 함."""
        pytest.skip("미구현")


class TestEventStudy:
    def test_pre_treatment_coefs_near_zero(self, synthetic_panel):
        """처리 이전 계수는 0 근처여야 함 (평행 추세)."""
        pytest.skip("미구현")


class TestSyntheticControl:
    def test_pre_period_match(self, synthetic_panel):
        """처리 전 기간 가중평균이 실제 처리집단을 잘 추적해야 함."""
        pytest.skip("미구현")
