from typing import TypedDict


class AdRequestParam(TypedDict):
    advertiser_id: str
    start_date: str
    end_date: str


TIKTOK_AD_DIMENSIONS = {
    "ID_DIMENSIONS": ["ad_id"],
    "TIME_DIMENSIONS": [
        "stat_time_day",
        "stat_time_hour",
    ],
    "TARGETING_DIMENSIONS": [
        "ad_type",
    ],
    "SEARCH_DIMENSIONS": [
        "search_terms",
    ],
    "ASSET_DIMENSIONS": ["page_id", "image_id"],
}

TIKTOK_AD_METRICS = {
    "ATTRIBUTES": [
        "advertiser_name",
        "advertiser_id",
        "campaign_name",
        "campaign_id",
        "adgroup_name",
        "adgroup_id",
        "objective_type",
        "placement_type",
    ],
    "PRODUCT_ATTRIBUTES": ["catalog_name", "product_set_name", "product_name"],
    "BASIC_AD_METRICS": [
        "spend",
        "impressions",
        "clicks",
        "cpc",
        "cpm",
        "ctr",
        "conversion",
        "cost_per_conversion",
        "conversion_rate",
        "result",
        "cost_per_result",
        "result_rate",
    ],
    "ADDITIONAL_AD_METRICS": [
        "reach",
        "real_time_conversion",
        "cost_per_1000_reached",
        "secondary_goal_result",
        "cost_per_secondary_goal_result",
        "secondary_goal_result_rate",
        "real_time_cost_per_conversion",
        "real_time_conversion_rate",
        "real_time_cost_per_result",
        "real_time_result_rate",
        "real_time_result",
    ],
    "VIDEO_AD_METRICS": [
        "video_play_actions",
        "engaged_view",
        "engaged_view_15s",
    ],
    "VIDEO_METRICS": [
        "video_watched_2s",
        # "video_watched_continuous_2s",
        "video_watched_6s",
        "average_video_play",
        "average_video_play_per_user",
        "video_views_p25",
        "video_views_p50",
        "video_views_p75",
        "video_views_p100",
    ],
    "ENGAGEMENT_METRICS": [
        "likes",
        "comments",
        "shares",
        "profile_visits",
        "follows",
    ],
    "SINGLE_IMAGE_METRICS": [
        "single_image_impressions",
        "single_image_impression_rate",
        "single_image_ctr",
        "clicks",
    ],
    "IN_APP_METRICS": [
        "add_to_wishlist",
        "add_to_wishlist_rate",
        "app_event_add_to_cart",
        "app_event_add_to_cart_rate",
        "checkout",
        "checkout_rate",
        "cost_per_checkout",
        "cost_per_purchase",
        "cost_per_add_to_wishlist",
        "cost_per_app_event_add_to_cart",
        "cost_per_registration",
        "cost_per_total_add_to_wishlist",
        "cost_per_total_app_event_add_to_cart",
        "cost_per_total_checkout",
        "cost_per_total_purchase",
        "cost_per_total_registration",
        "cost_per_total_view_content",
        "cost_per_view_content",
        "dpa_target_audience_type",
        "purchase",
        "purchase_rate",
        "registration",
        "registration_rate",
        "sales_lead",
        "total_active_pay_roas",
        "total_add_to_wishlist",
        "total_app_event_add_to_cart",
        "total_app_event_add_to_cart_value",
        "total_add_to_wishlist_value",
        "total_checkout",
        "total_checkout_value",
        "total_purchase",
        "total_purchase_value",
        "total_registration",
        "total_sales_lead",
        "total_sales_lead_value",
        "total_view_content",
        "total_view_content_value",
        "value_per_checkout",
        "value_per_total_purchase",
        "value_per_total_add_to_wishlist",
        "value_per_total_app_event_add_to_cart",
        "value_per_total_view_content",
        "view_content",
        "view_content_rate",
    ],
    "ATTRIBUTION_METRICS": [
        "cta_app_install",
        "cta_conversion",
        "cta_purchase",
        "cta_registration",
        "cost_per_cta_purchase",
        "cost_per_cta_registration",
        "cost_per_vta_conversion",
        "cost_per_vta_purchase",
        "cost_per_vta_registration",
        "vta_app_install",
        "vta_conversion",
        "vta_purchase",
        "vta_registration",
    ],
    "PAGE_EVENT_METRICS": [
        "complete_payment",
        "complete_payment_rate",
        "cost_per_complete_payment",
        "total_complete_payment_rate",
        "value_per_complete_payment",
        "cost_per_user_registration",
        "total_user_registration_value",
        "user_registration",
        "user_registration_rate",
        "value_per_user_registration",
        "cost_per_product_details_page_browse",
        "product_details_page_browse",
        "product_details_page_browse_rate",
        "total_product_details_page_browse_value",
        "value_per_product_details_page_browse",
        "cost_per_web_event_add_to_cart",
        "total_web_event_add_to_cart_value",
        "value_per_web_event_add_to_cart",
        "web_event_add_to_cart",
        "web_event_add_to_cart_rate",
        "cost_per_initiate_checkout",
        "initiate_checkout",
        "initiate_checkout_rate",
        "total_initiate_checkout_value",
        "value_per_initiate_checkout",
        "page_event_search",
        "cost_per_page_event_search",
        "page_event_search_rate",
        "value_per_page_event_search",
        "total_page_event_search_value",
        "cost_per_download_start",
        "download_start",
        "download_start_rate",
        "total_download_start_value",
        "value_per_download_start",
        "cost_per_on_web_add_to_wishlist",
        "on_web_add_to_wishlist",
        "on_web_add_to_wishlist_per_click",
        "total_on_web_add_to_wishlist_value",
        "value_per_on_web_add_to_wishlist",
    ],
    "SKAN_METRICS": [
        "skan_sales_lead",
        "skan_total_sales_lead",
        "skan_total_sales_lead_value",
    ],
    "SHOP_METRICS": [
        "onsite_shopping_roas",
        "onsite_shopping",
        "cost_per_onsite_shopping",
        "onsite_shopping_rate",
        "value_per_onsite_shopping",
        "total_onsite_shopping_value",
        "onsite_initiate_checkout_count",
        "cost_per_onsite_initiate_checkout_count",
        "onsite_initiate_checkout_count_rate",
        "value_per_onsite_initiate_checkout_count",
        "total_onsite_initiate_checkout_count_value",
        "onsite_on_web_detail",
        "cost_per_onsite_on_web_detail",
        "onsite_on_web_detail_rate",
        "value_per_onsite_on_web_detail",
        "total_onsite_on_web_detail_value",
        "onsite_on_web_cart",
        "cost_per_onsite_on_web_cart",
        "onsite_on_web_cart_rate",
        "value_per_onsite_on_web_cart",
        "total_onsite_on_web_cart_value",
    ]
}



