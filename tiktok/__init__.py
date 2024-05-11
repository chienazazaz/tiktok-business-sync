import os
from dotenv import load_dotenv

load_dotenv()

SANDBOX_ACCESS_TOKEN = os.getenv("TIKTOK_SANDBOX_ACCESS_TOKEN")
ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")
ENV = os.getenv("ENV")

from typing import Any, Dict

from tiktok.models.ad import Ad
from tiktok.models.adgroup import AdGroup
from tiktok.models.campaign import Campaign
from tiktok.models.creative_report import CreativeReport
from tiktok.models.video_insights import VideoInsight
from tiktok.models.ad_report import AD_REPORTING_MODELS
from tiktok.models.assets import Asset
from tiktok.models.business_center import BusinessCenter


TIKTOK_MODELS: Dict[str, Any] = {
    "user-assets": {"business_center": BusinessCenter},
    "business-assets": {"assets": Asset},
    "advertiser-assets": {
        "creative_report": CreativeReport,
        "video_insights": VideoInsight,
        "adgroup": AdGroup,
        "campaign": Campaign,
        "ad": Ad,
    },
    "reporting": [*AD_REPORTING_MODELS.keys()],
}
