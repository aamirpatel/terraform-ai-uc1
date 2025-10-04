import json
import sys


if not os.path.exists('output.json'):
    print("output.json not found. Please ensure it is generated before running this script.")
    sys.exit(1)

with open('output.json') as f:
    # existing logic

# Assume data is the string to be parsed
data = sys.stdin.read()
with open('output.json') as f:
    content = f.read().strip()
try:
    if content:
        data = json.loads(content)
    else:
        raise ValueError("output.json is empty, cannot parse JSON")
except json.JSONDecodeError as e:
        print(f"JSON decode failed: {e}")
        # handle error or exit
else:
    print("No data to parse")
    # handle empty input case

def analyze_plan(plan_file):
    with open(plan_file) as f:
        data = json.load(f)

    messages = []
    for res in data.get("resource_changes", []):
        if res["type"] == "aws_instance":
            for change in res["change"]["actions"]:
                if change == "create":
                    props = res["change"]["after"]
                    if props.get("instance_type") == "t2.micro":
                        messages.append(
                            f"⚠️ Consider upgrading `{res['name']}` from `t2.micro` to `t3.medium` for better performance."
                        )
    return messages

if __name__ == "__main__":
    findings = analyze_plan(sys.argv[1])
    for msg in findings:
        print(msg)
