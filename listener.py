import sys 
from flask import Flask, request, abort
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
  print("webhook"); sys.stdout.flush()
  if request.method == 'POST':
    print(request.json)
    data = {}
    with open("version.json","w") as f:
      data = json.load(f)
    print(data)
    return '', 200
  else:
    abort(400)


if __name__ == '__main__':
  app.run()

