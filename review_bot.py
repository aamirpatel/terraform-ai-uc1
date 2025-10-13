import json
import os
import sys

def load_tfplan_json(file_path):
    # Example: Check if the file is empty before parsing
if [ ! -s output.json ]; then
  echo "JSON output is empty. Terraform may have failed or produced no output."
  exit 1
fi
jq . output.json

    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, "r") as f:
        content = f.read().strip()
        if not content:
            print("Error: tfplan.json is empty.")
            sys.exit(1)

        try:
            data = json.loads(content)
            return data
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON - {e}")
            sys.exit(1)

def review_resources(data):
    if "resource_changes" not in data:
        print("No resource changes found in the plan.")
        return

    print("Reviewing resource changes:")
    for change in data["resource_changes"]:
        action = change.get("change", {}).get("actions", [])
        resource_type = change.get("type")
        resource_name = change.get("name")
        print(f"- {resource_type}.{resource_name}: {', '.join(action)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 review_bot.py tfplan.json")
        sys.exit(1)

    file_path = sys.argv[1]
    tfplan_data = load_tfplan_json(file_path)
    review_resources(tfplan_data)
