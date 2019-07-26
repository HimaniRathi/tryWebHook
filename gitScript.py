import json

data = {}
with open("version.json","r") as f:
    data = json.loads(f.read())
data["version"] = data["version"] + 1
with open("version.json","w") as f:
    f.write(json.dumps(data))