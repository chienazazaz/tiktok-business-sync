from datetime import datetime, timedelta
import json
from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel


from tiktok.auth.auth import set_access_token
from tiktok.pipelines import create_tasks_pipelines, run_pipeline

app = FastAPI()


class DefaultRequestParams(BaseModel):
    start_date: Union[str, None] = None
    end_date: Union[str, None] = None
    business_ids: Union[List[str], None] = None


class PipelineRequestParams(DefaultRequestParams):
    name: str
    type: Union[str, None] = None
    business_ids: Union[List[str], None] = None
    bc_id: Union[str, None] = None
    advertiser_ids: Union[List[str],None] = None
    advertiser_id: Union[str,None] = None


@app.post("/tasks/{type}", tags=["create tasks"], response_model=None)
def creatTasksHandler(request: DefaultRequestParams, type: str):
    params = json.loads(request.model_dump_json())
    start_date, end_date, business_ids = params.get("start_date"), params.get("end_date"),params.get("business_ids")
    if not start_date:
        start_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    if not end_date:
        end_date = datetime.now().strftime("%Y-%m-%d")
    return create_tasks_pipelines(
        {"start_date": start_date, "end_date": end_date},
        type=str(type),
        business_ids=business_ids,
        name=str(type),
    )

@app.get("/callback", tags=["set access-token"], response_model=None)
def callbackHandler(auth_code:str):
    set_access_token(auth_code)
    return {"status": "success"}


@app.post("/", tags=["run pipeline"], response_model=None)
def runPipelineHandler(request: PipelineRequestParams):
    params = json.loads(request.model_dump_json())
    print(params)
    result = run_pipeline(params)
    return result
