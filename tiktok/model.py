from typing import Callable, List, Dict, Optional

from tiktok.client import TiktokClient


class Model:
    schema = [{"name": "data", "type": "JSON"}]

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    # def transform(self, data: List[Dict]) -> List[Dict]:
    #     return {"data": data}

    def get(self, param: Optional[Dict], request_data: Optional[Dict]=None) -> List[Dict]:
        data = []
        param["page_size"] = param.get("page_size") or 50

        def _get(param: Optional[Dict], request_data: Optional[Dict]=None) -> List[Dict]:
            response: Dict = TiktokClient().get(path=self.path, param=param, data=request_data).get("data")
            # print(response)
            # response = response_.get("data")
            result, page_info = response.get("list"), response.get("page_info")
            data.extend(result) if result else None
            if page_info.get("page") < page_info.get("total_page"):
                return _get({**param, "page": page_info.get("page") + 1}, request_data={})
            else:
                return data

        return _get(param=param, request_data=request_data)
