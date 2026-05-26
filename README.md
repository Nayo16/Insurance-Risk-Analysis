# Insurance Risk Analytics — ACIS

Project scaffold for Week 3: insurance risk analytics for AlphaCare Insurance Solutions (ACIS).

See the project plan and steps in the task description.

## Quickstart

- Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- Development branches: `task-1`, `task-2`.

## DVC

This repo tracks the dataset with DVC. To reproduce the data pipeline:

```powershell
pip install dvc
# initialize dvc once
dvc init
mkdir -p ../dvc_local_storage
# add local remote
dvc remote add -d localstorage ../dvc_local_storage
# track dataset
dvc add data/insurance_data.csv
# push to the local remote
dvc push
```
