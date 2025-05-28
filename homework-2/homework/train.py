import os
import pickle
import click
import mlflow

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):

    mlflow.set_tracking_uri("sqlite:///homework/mlops-homework.db")
    mlflow.set_experiment("mlops-homework-rf")

    mlflow.sklearn.autolog()
    with mlflow.start_run():
        X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
        X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))
        
        experiment_limit = 3009173
        
        X_train = X_train[:experiment_limit]
        y_train = y_train[:experiment_limit]
        X_val = X_val[:experiment_limit]
        y_val = y_val[:experiment_limit]

        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        rmse = root_mean_squared_error(y_val, y_pred)


if __name__ == '__main__':
    run_train()
