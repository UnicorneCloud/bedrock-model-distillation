# bedrock-model-distillation

## Install

```
poetry install
export PYTHONPATH=`pwd`
```

## How it works:

1. Change all constants in file consts.py

2. Run `poetry run python src/prepare_training.py`

3. Run `poetry run python src/start_job.py` take note of the job arn and role name created. You will need them later

4. Change the job_arn in `monitor_job.py`. Run `poetry run python src/monitor_job.py` until the job is completed or check in the AWS Console and wait for completion

5. Change the job_arn in `deploy_model.py`. Run `poetry run python src/deploy_model.py`

## Clean up

Run `poetry run python src/clean_up.py`
