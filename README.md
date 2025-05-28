# MLOps Zoomcamp

This repository is a learning ground for MLOps, based on the excellent [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) by [DataTalks.Club](https://datatalks.club/).

## Objective

- To gain hands-on experience with MLOps tools and workflows
- To follow along with the MLOps Zoomcamp curriculum
- To build and deploy ML models in a production-like environment

## Contents

- Jupyter notebooks and scripts covering:
  - Experiment tracking
  - Model packaging
  - CI/CD
  - Deployment
  - Monitoring
  - and more...

## MLFlow
To use MLflow for experiment tracking:

- install `mlflow` with `pip install mlflow`
- start the server with sqlite backend

```bash
mlflow ui --host 0.0.0.0 --backend-store-uri sqlit:///mlflow.db
```

- Wrap the training loop with `mlflow.start_run()`
- log params with `mlflow.log_param('key', 'value')` or `mlflow.log_params(param_dict)`
- log metrics with `mlflow.log_metric('key', 'value')` or `mlflow.log_params(metric_dict)`
- set tags for filtering purposes, like `mlflow.set_tag('model', 'xgboost')`
- `mlflow` support automatic logging for some custom models/frameworks with `autolog`, i.e. for `xgboost`, we can use `mlflow.xgboost.autolog()`
- `mlflow.search_experiments()` list all the experiments, if no argument (experiment_id) is provided
- `mlflow.get_run(run_id)` provides detailed info for a given run

### Model Management

- log model as an artifact `mlflow.log_artifact(local_path_to_store_artifact, artifact_path_for_mlflow)`
- log model using `mlflow.<framework>.log_model(model, artifact_path_for_mlflow)`, i.e. for xgboost, we can store using `mlflow.xgboost.log_model(model, artifact_path='xgboost_mlflow/')`

- `mlflow` provides snippets as well for loading model and prediction

## Acknowledgements

Special thanks to the [DataTalks.Club](https://datatalks.club/) community and [Alexey Grigorev](https://www.linkedin.com/in/agrigorev/) for creating and maintaining the MLOps Zoomcamp.

