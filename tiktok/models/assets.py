from typing import Dict, List
from tiktok.model import Model


class Asset(Model):
    asset_types = ["ADVERTISER", "CATALOG", "TT_ACCOUNT", "TIKTOK_SHOP"]

    def __init__(self):
        self.name = "assets"
        self.path = "bc/asset/get/"

    def transform(self, data):
        return data

    def get(self, param: Dict,*args,**kwargs) -> List[Dict]:
        data = []
        for asset_type in self.asset_types:
            result = super().get({**param, "asset_type": asset_type},data={})
            data.extend(result) if result else None
        return self.transform(data)

    def getAdAccounts(self, param: Dict,*args,**kwargs) -> List[str]:
        accounts = super().get({**param, "asset_type": "ADVERTISER"},data={})
        return list(account.get("asset_id") for account in accounts)