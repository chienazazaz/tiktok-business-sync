from typing import List, Dict
from google.cloud import bigquery

from gcloud import DATASET

client = bigquery.Client()

def load(data:List[Dict], schema, name):
    job_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        create_disposition=bigquery.CreateDisposition.CREATE_IF_NEEDED
    )
    result = client.load_table_from_json(json_rows=data, destination=f"{DATASET}.{name}", job_config=job_config).result()

    return result.result()

    
    