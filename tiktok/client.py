import json
from requests import request
from urllib.parse import urlunparse
from typing import Dict

from gcloud.secret_manager import get_secret
from tiktok import ENV, SANDBOX_ACCESS_TOKEN, ACCESS_TOKEN


def build_url(path: str, query="") -> str:
    scheme, netloc = "https", "business-api.tiktok.com"
    return urlunparse((scheme, netloc, "/open_api/v1.3/" + path, "", query, ""))


class TiktokClient:

    def __init__(self):
        self.access_token = ACCESS_TOKEN or get_secret("tiktok-access-token")
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
        ).json()

        if response.get("code") != 0:
            raise Exception(
                {"code": response.get("code"), "message": response.get("message")}
            )

        return response
