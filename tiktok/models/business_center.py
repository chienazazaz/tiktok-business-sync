from typing import Callable, Dict, List
from tiktok.model import Model


class BusinessCenter(Model):
    def __init__(self):
        self.name = "business_center"
        self.path = "bc/get/"

    def transform(self,data):
        # print(data)
        return list(row.get("bc_info") for row in data)

    def get(self, param: Dict,*args,**kwargs) -> List[Dict]:
        return self.transform(super().get())