from typing import Dict, List

from tiktok.model import Model
from tiktok.models import AdRequestParam


class VideoInsight(Model):

    def __init__(self):
        self.name = "video_insight"
        self.path = "creative/report/get/"

    def get(self, param: AdRequestParam, *args, **kwargs) -> List[Dict]:
        param["page_size"] = 1000
        param["report_type"] = "VIDEO_INSIGHT"
        return super().get(param)
