import json
from typing import Dict, List

from tiktok.model import Model
from tiktok.models import TIKTOK_AD_METRICS, AdRequestParam

CREATIVE_REPORT_METRICS = list(
    filter(
        lambda x: x
        not in [
            "result",
            "cost_per_result",
            "result_rate",
            "total_active_pay_roas",
            "dpa_target_audience_type",
            "download_start",
            "average_video_play_per_user",
        ],
        [
            *TIKTOK_AD_METRICS["BASIC_AD_METRICS"],
            *TIKTOK_AD_METRICS["VIDEO_METRICS"],
            *TIKTOK_AD_METRICS["VIDEO_AD_METRICS"],
            *TIKTOK_AD_METRICS["IN_APP_METRICS"],
            *TIKTOK_AD_METRICS["PAGE_EVENT_METRICS"],
        ],
    )
)


class CreativeReport(Model):
    material_types = ["VIDEO", "IMAGE", "INSTANT_PAGE"]

    def __init__(self, ):
        self.name = "creative_report"
        self.path = "creative/report/get/"

    def get(self, param: AdRequestParam, *args, **kwargs) -> List[Dict]:
        param["page_size"] = 1000
        param["metrics_fields"] = json.dumps(CREATIVE_REPORT_METRICS)
        data = []
        for material_type in self.material_types:
            result = super().get({**param, "material_type": material_type})
            data.extend(result) if result else None
        return data
