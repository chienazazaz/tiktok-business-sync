from typing import Any, Dict
from gcloud.bigquery import load
from gcloud.create_tasks import create_tasks
from tiktok.model import Model
from tiktok.models import TIKTOK_MODELS
from tiktok.models.ad_reporting import AdReporting
from datetime import datetime, timezone

from tiktok.models.assets import Asset


def get_model(name: str, **kwargs) -> Model:
    if kwargs.get("type") == "reporting":
        return AdReporting(name)
    return TIKTOK_MODELS[name]()


def run_pipeline(params:Dict) -> Dict[str,Any]:
    # print(params)
    model = get_model(
        params.get("name"),
        type = params.get("type")
    )

    data = model.get(param=params, data={})
    _batched_at = datetime.now(timezone.utc)
    result = load(
        map(lambda x: {"data": x, "_batched_at": _batched_at.isoformat()}, data),
        schema=[*model.schema, {"name": "_batched_at", "type": "TIMESTAMP"}],
        name=f"p_{model.name}__{_batched_at.strftime('%Y%m%d')}",
    )

    return {"result": result.done(), "table": f"{model.name}", "num_inserted": len(data)}


def create_tasks_pipelines(param: Dict, **kwargs) -> Dict[str,int]:
    if kwargs.get("type") == "reporting":
        accounts = (
            {"advertiser_ids": list(
                account
                for account in Asset().getAdAccounts({"bc_id": f"{business_id}"})
            ),"bc_id":business_id}
            for business_id in kwargs.get("business_ids")
        )

        models = TIKTOK_MODELS["reporting"]
        payloads = list(
            {**param, **account, "name": model,"type":"reporting"}
            for account in accounts
            for model in models
        )
        print(payloads)
    elif kwargs.get("name") == "asset":
        payloads = list(
            {**param, "bc_id": business_id, "name": "asset"}
            for business_id in kwargs.get("business_ids")
        )
    else:
        payloads = [{**param, "name": kwargs.get("name")}]
    result = create_tasks(
        payloads=payloads,
        nameFn=(
            lambda p: "".join(
                [
                    p.get("name"),
                    "-",
                    p.get("bc_id") or "",
                ]
            )
        ),
    )

    return {"num_tasks":result}
