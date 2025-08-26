import mlflow
import mlflow.sklearn

# Run ID jo tumhare MLflow UI me show ho raha hai
run_id = "544c4173775c4af6954bb0b29416626f"

# Model path (artifact_path jo tumne log karte waqt diya tha)
model_uri = f"runs:/{run_id}/model"

# Load the model back
loaded_model = mlflow.sklearn.load_model(model_uri)
# print(loaded_model)

