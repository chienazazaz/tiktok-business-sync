import json
from typing import Dict, List

from tiktok.model import Model
from tiktok.models import TIKTOK_AD_METRICS, AdRequestParam



AD_REPORTING_MODELS = {
    "AD_REPORT_DAILY": {
        "report_type": "BASIC",
        "data_level": "AUCTION_AD",
        "dimensions": ["ad_id", "stat_time_day"],
        "metrics": [
            *TIKTOK_AD_METRICS["ATTRIBUTES"],
            *TIKTOK_AD_METRICS["BASIC_AD_METRICS"],
            *TIKTOK_AD_METRICS["ADDITIONAL_AD_METRICS"],
            *TIKTOK_AD_METRICS["VIDEO_AD_METRICS"],
            *TIKTOK_AD_METRICS["VIDEO_METRICS"],
            *TIKTOK_AD_METRICS["ENGAGEMENT_METRICS"],
            *TIKTOK_AD_METRICS["IN_APP_METRICS"],
            *TIKTOK_AD_METRICS["PAGE_EVENT_METRICS"],
            *TIKTOK_AD_METRICS["ATTRIBUTION_METRICS"],
            *TIKTOK_AD_METRICS["SKAN_METRICS"],
        ],
    },
    # "AD_REPORT_HOURLY": {
    #     "report_type": "BASIC",
    #     "data_level": "AUCTION_AD",
    #     "dimensions": ["ad_id", "stat_time_hour"],
    #     "metrics": [
    #         *TIKTOK_AD_METRICS["ATTRIBUTES"],
    #         *TIKTOK_AD_METRICS["BASIC_AD_METRICS"],
    #         *TIKTOK_AD_METRICS["ADDITIONAL_AD_METRICS"],
    #         *TIKTOK_AD_METRICS["VIDEO_AD_METRICS"],
    #         *TIKTOK_AD_METRICS["VIDEO_METRICS"],
    #         *TIKTOK_AD_METRICS["ENGAGEMENT_METRICS"],
    #         *TIKTOK_AD_METRICS["IN_APP_METRICS"],
    #         *TIKTOK_AD_METRICS["PAGE_EVENT_METRICS"],
    #         *TIKTOK_AD_METRICS["ATTRIBUTION_METRICS"],
    #     ],
    # },
    "IMAGE_REPORT": {
        "report_type": "BASIC",
        "data_level": "AUCTION_AD",
        "dimensions": ["ad_id", "stat_time_day", "image_id"],
        "metrics": [
            *TIKTOK_AD_METRICS["ATTRIBUTES"],
            *TIKTOK_AD_METRICS["SINGLE_IMAGE_METRICS"],
        ],
    },
    "SEARCH_REPORT": {
        "report_type": "BASIC",
        "data_level": "AUCTION_AD",
        "dimensions": ["ad_id", "stat_time_day", "search_terms"],
        "metrics": [
            *TIKTOK_AD_METRICS["ATTRIBUTES"],
            *TIKTOK_AD_METRICS["BASIC_AD_METRICS"],
            *TIKTOK_AD_METRICS["VIDEO_AD_METRICS"],
        ],
    },
    "AD_AGE_GENDER_REPORT": {
        "report_type": "AUDIENCE",
        "data_level": "AUCTION_AD",
        "dimensions": ["ad_id", "stat_time_day", "age", "gender"],
        "metrics": [
            *TIKTOK_AD_METRICS["ATTRIBUTES"],
            *TIKTOK_AD_METRICS["BASIC_AD_METRICS"],
            *TIKTOK_AD_METRICS["VIDEO_METRICS"],
            *TIKTOK_AD_METRICS["ENGAGEMENT_METRICS"],
        ],
    },
    # "DSA_REPORT": {
    #     "report_type": "CATALOG",
    #     "data_level": "AUCTION_AD",
    #     "dimensions": ["ad_id", "stat_time_day","product_id"],
    #     "metrics": [
    #         *TIKTOK_AD_METRICS["ATTRIBUTES"],
    #         *TIKTOK_AD_METRICS["PRODUCT_ATTRIBUTES"],
    #         *TIKTOK_AD_METRICS["BASIC_AD_METRICS"],
    #     ],
    # },
}


class AdReport(Model):

    def __init__(self,name:str):
        self.name = name
        self.path = "report/integrated/get/"

    def transform(self, data):
        return data

    def get(self, param: AdRequestParam,*args,**kwargs) -> List[Dict]:
        param["page_size"] = 1000
        param["metrics"] = json.dumps(AD_REPORTING_MODELS[self.name].get("metrics"))
        param["dimensions"] = json.dumps(AD_REPORTING_MODELS[self.name].get("dimensions"))
        param["report_type"] = AD_REPORTING_MODELS[self.name].get("report_type")
        param["data_level"] = AD_REPORTING_MODELS[self.name].get("data_level")
        if param.get("advertiser_ids"):
            param["advertiser_ids"] = json.dumps(param.get("advertiser_ids"))
        return super().get(param=param)
