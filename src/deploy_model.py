import datetime
from src.consts import bedrock_client

job_arn = "change me"

# Deploy the distilled model
custom_model_id = bedrock_client.get_model_customization_job(jobIdentifier=job_arn)['outputModelArn']
distilled_model_name = f"distilled-model-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

provisioned_model_id = bedrock_client.create_provisioned_model_throughput(
    modelUnits=1,
    provisionedModelName=distilled_model_name,
    modelId=custom_model_id
)['provisionedModelArn']

print("Provisioned Model ID: ", provisioned_model_id)