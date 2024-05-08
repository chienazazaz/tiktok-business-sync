import json

import requests
from gcloud.secret_manager import set_secret
from tiktok.auth import APP_ID, APP_SECDRET
from tiktok.client import build_url


def exchange_access_token(auth_code: str) -> str:
    url = build_url("oauth2/access_token/")
    headers = {
        "Content-Type": "application/json",
    }
    rsp = requests.request(
        method="POST",
        url=url,
        headers=headers,
        data=json.dumps(
            {"app_id": APP_ID, "secret": APP_SECDRET, "auth_code": auth_code}
        ),
    ).json()

    if rsp["code"] != 0 or not rsp:
        raise Exception(rsp["message"])
    return rsp["data"].get("access_token")


def set_access_token(auth_code: str) -> None:
    access_token = exchange_access_token(auth_code)
    set_secret("tiktok-access-token", access_token)
    return
