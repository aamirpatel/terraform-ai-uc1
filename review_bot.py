import json
import os

file_path = "tfplan.json"

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found.")

# Read and validate content
with open(file_path, "r") as f:
    content = f.read().strip()
    if not content:
        raise ValueError("tfplan.json is empty or invalid.")

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")
`
