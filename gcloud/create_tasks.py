from typing import List, Dict, Callable
from uuid import uuid4
from google.cloud import tasks_v2
from google.cloud.tasks_v2 import types

from gcloud import LOCATION, PUBLIC_URL, QUEUE, PROJECT_ID, SERVICE_ACCOUNT

client = tasks_v2.CloudTasksClient()

def create_tasks(payloads: List[Dict], nameFn: Callable) -> int:
    responses: List[Dict] = []
    for payload in payloads:
        responses.append(
            client.create_task(
                parent=client.queue_path(PROJECT_ID, LOCATION, QUEUE),
                task={
                    "name": client.task_path(
                        PROJECT_ID, LOCATION, QUEUE, f"{nameFn(payload)}-{uuid4()}"
                    ),
                    "http_request": {
                        "url": f"{PUBLIC_URL}/",
                        "http_method": "POST",
                        "headers": {"Content-Type": "application/json"},
                        "body": str(payload).encode(),
                        "oidc_token": {
                            "service_account_email": SERVICE_ACCOUNT,
                        },
                    },
                },
            )
        )

    return len(responses)
