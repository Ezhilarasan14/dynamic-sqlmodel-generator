from typing import Dict, Any
import json
from sqlmodel import SQLModel, Field

# Function to read JSON from a file and return parsed data
def read_json_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)

# Read the JSON input from the file
input_data = read_json_file('input_data.json')
table_name = input_data["table_name"]
fields = input_data["fields"]

# Map string types to actual Python types
type_mapping = {"int": int, "str": str, "bool": bool, "float": float}

# Create attributes with primary key
annotations: Dict[str, Any] = {}
attributes = {
    "__annotations__": annotations,
    "__tablename__": table_name.lower(),
    "model_config": {"table": True},
}

for field_name, field_type in fields.items():
    python_type = type_mapping[field_type]
    annotations[field_name] = python_type
    attributes[field_name] = Field(default=None, primary_key=(field_name == 'id'))

# Create model class
ModelClass = type(table_name, (SQLModel,), attributes)

# Instantiate the model (example values, adjust as needed)
new_user = ModelClass(id=1, name="Alice", email="alice@example.com", age=30, is_active=True)
print(new_user)
