import json
from requests import request
from urllib.parse import urlunparse
from typing import Dict

from gcloud.secret_manager import get_secret
from tiktok import ENV, SANBOX_ACCESS_TOKEN


def build_url(path: str, query="") -> str:
    scheme, netloc = "https", "business-api.tiktok.com" if ENV == 'prod' else "sandbox-ads.tiktok.com"
    return urlunparse((scheme, netloc, "/open_api/v1.3/" + path, "", query, ""))


class TiktokClient:

    def __init__(self):
        self.access_token = get_secret("tiktok-access-token") if ENV =='prod' else SANBOX_ACCESS_TOKEN
        self.headers = {
            "Content-Type": "application/json",
            "Access-Token": f"{self.access_token}",
        }

    def get(self, path: str, param: Dict, data: Dict) -> Dict:
        url = build_url(path)
        response = request(
            method="GET",
            url=url,
            params=param,
            data=json.dumps(data),
            headers=self.headers,
        )
        # print(response.url)
        # print(response.text)
        # print(response.headers)
        return response.json()
