from src.consts import bedrock_client

# Record the distillation job arn
job_arn = "change me"

# print job status
job_status = bedrock_client.get_model_customization_job(jobIdentifier=job_arn)["status"]
print(job_status)