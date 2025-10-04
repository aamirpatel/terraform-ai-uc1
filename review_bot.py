import json
import sys

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
