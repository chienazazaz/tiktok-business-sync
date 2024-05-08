from datetime import datetime
import json
from tkinter import N
from typing import List, Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel


from tiktok.pipelines import create_tasks_pipelines, run_pipeline

app = FastAPI()


class DefaultRequestParams(BaseModel):
    start_date: Union[str, None] = None
    end_date: Union[str, None] = None


class PipelineRequestParams(DefaultRequestParams):
    name: str
    type: Union[str, None] = None
    business_ids: Union[List[str], None] = None
    bc_id: Union[str, None] = None
    advertiser_ids: Union[List[str],None] = None
    advertiser_id: Union[str,None] = None


@app.post("/tasks/{type}", tags=["create tasks"], response_model=None)
def creatTasksHandler(param: DefaultRequestParams, type: str):
    start_date, end_date = param.start_date, param.end_date
    if not start_date:
        start_date = datetime.now().strftime("%Y-%m-%d")
    if not end_date:
        end_date = datetime.now().strftime("%Y-%m-%d")
    return create_tasks_pipelines(
        {"start_date": start_date, "end_date": end_date},
        type=str(type),
        business_ids=["7362106247526563856"],
        name=str(type),
    )


@app.post("/", tags=["run pipeline"], response_model=None)
def runPipelineHandler(request: PipelineRequestParams):
    
    params = request.model_dump_json()
    params = json.loads(params)
    result = run_pipeline(params)
    return result
