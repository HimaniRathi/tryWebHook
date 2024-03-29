import sys 
from flask import Flask, request, abort
import json
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  print("webhook"); sys.stdout.flush()
  temp = request.json
  if request.method == 'POST' and temp["action"] == "closed" and temp["pull_request"]["merged"]:
    print(request.json)
    os.system('bash script.sh')
    return '', 200
  else:
    abort(400)

if __name__ == '__main__':
  app.run()

