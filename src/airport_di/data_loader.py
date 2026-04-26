"""
패널 데이터 로더

수원·광주·대구 등 군공항 사례별 패널 데이터를 통합 형식으로 로드한다.

데이터 소스:
    - MOLIT 실거래가 (아파트 매매)
    - KB 시세 / 부동산원 매매가격지수
    - 통계청 인구·경제총조사 (시군구 단위)
    - SGIS 행정경계 (V-World)
    - 항공기 소음도 (환경부 항공기소음포털)

패널 구조:
    columns: [region_code, year_month, treatment_dummy, post_dummy, 
              outcome_vars..., covariates...]
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Literal, Optional
from dataclasses import dataclass

import pandas as pd
import geopandas as gpd

logger = logging.getLogger(__name__)

CaseStudy = Literal["suwon", "gwangju", "daegu", "gimpo", "synthetic"]


@dataclass
class CaseConfig:
    """사례별 분석 설정."""

    name: str
    treatment_regions: list[str]      # 처리집단 시군구 코드
    control_regions: list[str]        # 통제집단 시군구 코드
    treatment_year: int               # 정책 발효 연도
    pre_window: int = 5               # 사전 관측 기간 (연)
    post_window: int = 5              # 사후 관측 기간 (연)
    spatial_buffer_km: float = 5.0    # 공간 영향권 반경


# ----------------------------------------------------------------------
# 사례 설정 (참조용)
# ----------------------------------------------------------------------
CASE_CONFIGS: dict[str, CaseConfig] = {
    "suwon": CaseConfig(
        name="수원 군공항 이전",
        treatment_regions=["41110", "41115"],   # 수원시 영통/팔달
        control_regions=["41210", "41220"],     # 광명/안양 (유사 도시)
        treatment_year=2025,
        spatial_buffer_km=5.0,
    ),
    "gwangju": CaseConfig(
        name="광주 군공항 이전",
        treatment_regions=["29170"],            # 광산구
        control_regions=["29110", "29140"],
        treatment_year=2024,
    ),
    "daegu": CaseConfig(
        name="대구 군공항 이전",
        treatment_regions=["27170"],            # 동구
        control_regions=["27200", "27230"],
        treatment_year=2023,
    ),
    "gimpo": CaseConfig(
        name="김포공항 소음권",
        treatment_regions=["41280"],            # 김포시
        control_regions=["41290", "41360"],
        treatment_year=None,                    # 시점이 아닌 거리 기반
    ),
}


def load_panel(
    case: CaseStudy = "suwon",
    data_dir: str = "data/processed",
) -> pd.DataFrame:
    """
    사례별 정제된 패널 데이터 로드.

    Args:
        case: 분석 사례 ('suwon' | 'gwangju' | 'daegu' | 'gimpo' | 'synthetic')
        data_dir: 정제된 parquet 파일 위치

    Returns:
        long-format 패널 DataFrame
        Required columns:
            - region_code: str
            - year_month: pd.Period[M] or YYYYMM int
            - treatment: 0/1 (treatment_regions에 포함되는 행 = 1)
            - post: 0/1 (year >= treatment_year인 행 = 1)
            - outcome (예: log_price_per_sqm)
            - covariates (인구, 소득, 건축연도 평균 등)
    """
    raise NotImplementedError(
        "TODO: pd.read_parquet(f'{data_dir}/{case}_panel.parquet'); "
        "또는 case='synthetic'이면 generate_synthetic_panel() 호출"
    )


def load_synthetic_panel(
    n_treated: int = 1,
    n_control: int = 30,
    pre_periods: int = 60,
    post_periods: int = 24,
    treatment_effect: float = -0.05,
    seed: int = 42,
) -> pd.DataFrame:
    """
    합성통제법 시뮬레이션용 인공 패널 생성.

    트렌드 + 계절성 + 처리효과를 가진 가짜 데이터로
    DID 추정기 정확도 검증에 사용.

    Returns:
        ['region_code', 'period', 'treatment', 'post', 'outcome'] 컬럼
    """
    raise NotImplementedError(
        "TODO: np.random.seed; 통제군 N개 베이스 trend + 처리군에 post 시점 +effect 추가"
    )


def load_boundary_geo(case: CaseStudy) -> gpd.GeoDataFrame:
    """사례별 처리·통제 지역 행정경계 GeoDataFrame 반환."""
    raise NotImplementedError(
        "TODO: SGIS shapefile에서 region_code IN (treatment + control) 필터"
    )
