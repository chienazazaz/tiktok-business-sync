from datetime import datetime, timedelta
import json
from typing import Callable, Dict, List
from tiktok.model import Model


class Campaign(Model):
    def __init__(self):
        self.name = "campaign"
        self.path = "campaign/get/"


    def get(self, param: Dict, *args, **kwargs) -> List[Dict]:
        param["filtering"] = json.dumps(
            {
                "creation_filter_start_time": (
                    datetime.strptime(param.get("end_date"), "%Y-%m-%d")
                    - timedelta(days=90)
                ).strftime("%Y-%m-%d 23:59:59"),
                "creation_filter_end_time": param.get("end_date") + " 00:00:00",
            }
        )
        return super().get(param=param)
