from src.consts import bucket_name, bedrock_client
from src.utils import delete_distillation_buckets, delete_role_and_attached_policies

role_name = "change"
provisioned_model_id = ""

# # delete bucket and dataset
delete_distillation_buckets(bucket_name)

# delete role and its policy:
delete_role_and_attached_policies(role_name=role_name)

# delete provisioned throughput:
response = bedrock_client.delete_provisioned_model_throughput(provisionedModelId=provisioned_model_id)