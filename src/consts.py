import boto3

# Create Bedrock client
bedrock_client = boto3.client(service_name="bedrock")

# Create runtime client for inference
bedrock_runtime = boto3.client(service_name='bedrock-runtime')

# Region and accountID
session = boto3.session.Session()
region = session.region_name
sts_client = session.client('sts')
account_id = sts_client.get_caller_identity()['Account']

# define bucket you want to create and upload the dataset to:
bucket_name='unicorne-reinvent-demo-model-distillation-1' # Replace by your bucket name
data_prefix = 'data' # Replace by your defined prefix

# configure teacher nd student model
teacher_model = "amazon.nova-pro-v1:0"
student_model_micro = "amazon.nova-micro-v1:0:128k"

system_message = """You are a specialized financial analyst assistant trained to analyze SEC filings, financial documents, and regulatory submissions. Your role is to:
- Extract and interpret key information from 10-K, 10-Q, and other SEC filings
- Provide accurate, factual responses based solely on the provided document context
- Focus on specific financial, legal, and corporate governance details
- Present information clearly and concisely without speculation
- Maintain accuracy in reporting numbers, dates, and regulatory details
When responding, only use information explicitly stated in the provided context."""

input_data_file = './src/sample/sample.jsonl'
output_data_file = './src/sample/model_distillation_dataset.jsonl'