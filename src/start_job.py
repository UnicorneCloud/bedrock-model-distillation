from datetime import datetime
from src.utils import create_s3_bucket, upload_training_data_to_s3, create_model_distillation_role_and_permissions
from src.consts import bucket_name, data_prefix, account_id, output_data_file, bedrock_client, teacher_model, student_model_micro

# Generate unique names for the job and model
job_name = f"distillation-job-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
model_name = f"distilled-model-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Configure models and IAM role
role_name, role_arn = create_model_distillation_role_and_permissions(bucket_name=bucket_name, account_id=account_id)

# creating training data bucket
create_s3_bucket(bucket_name=bucket_name)

# Specify S3 locations
training_data = upload_training_data_to_s3(bucket_name, output_data_file, prefix=data_prefix)
output_path = f"s3://{bucket_name}/output/"

# Set maximum response length
max_response_length = 1000

response = bedrock_client.create_model_customization_job(
    jobName=job_name,
    customModelName=model_name,
    roleArn=role_arn,
    baseModelIdentifier=student_model_micro,
    customizationType="DISTILLATION",
    trainingDataConfig={
        "s3Uri": training_data
    },
    outputDataConfig={
        "s3Uri": output_path
    },
    customizationConfig={
        "distillationConfig": {
            "teacherModelConfig": {
                "teacherModelIdentifier": teacher_model,
                "maxResponseLengthForInference": max_response_length
            }
        }
    }
)

print("Bucket Name: ", bucket_name)
print("Role Name: ", role_name)
print("Response: ", response)
print("Job ARN: ", response["jobArn"])