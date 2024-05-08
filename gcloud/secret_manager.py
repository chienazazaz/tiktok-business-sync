from typing import Any
from google.cloud import secretmanager

from gcloud import PROJECT_ID

client = secretmanager.SecretManagerServiceClient()


def get_secret(name: str) -> Any:
    secret = client.access_secret_version(
        request={"name": f"projects/{PROJECT_ID}/secrets/{name}/versions/latest"}
    )
    return secret.payload.data.decode("utf-8")


def set_secret(name: str, value: str) -> None:
    try:
        client.get_secret(request={"name": f"projects/{PROJECT_ID}/secrets/{name}"})
    except Exception:
        client.create_secret(
            request={
                "parent": f"projects/{PROJECT_ID}",
                "secret_id": name,
                "secret": {"replication": {"automatic": {}}},
            }
        )
    client.add_secret_version(
        request={
            "parent": f"projects/{PROJECT_ID}/secrets/{name}",
            "payload": {"data": value.encode()},
        }
    )
    return
