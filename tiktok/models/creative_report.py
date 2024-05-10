from typing import Dict, List

from tiktok.model import Model
from tiktok.models import AdRequestParam


class CreativeReport(Model):
    material_types = ["VIDEO", "IMAGE", "INSTANT_PAGE"]

    def __init__(self):
        self.name = "creative_report"
        self.path = "creative/report/get/"

    def transform(self, data):
        return data

    def get(self, param: AdRequestParam, *args, **kwargs) -> List[Dict]:
        param["page_size"] = 1000
        data = []
        for material_type in self.material_types:
            result = super().get(
                {**param, "material_type": material_type}, request_data={}
            )
            data.extend(result) if result else None
        return data
