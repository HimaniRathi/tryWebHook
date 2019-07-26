import sys 
from flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  print("webhook"); sys.stdout.flush()
  if request.method == 'POST':
    print(request.json)
    updateVersion()
    return '', 200
  else:
    abort(400)

def updateVersion():
  data = {}
  with open("version.json","r") as f:
    data = json.loads(f.read())
  data["version"] = data["version"] + 1
  with open("version.json","w") as f:
    f.write(json.dumps(data))

if __name__ == '__main__':
  app.run()

