import sys 
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
 print("webhook"); sys.stdout.flush()
 if request.method == 'POST':
  #print(request.json)
  f = open("version", 'r')
  line = f.read()
  line = f.read()
  print(line)
  if line[: 9] == '"version"':
   print(line[13])   
  return '', 200
 else:
  abort(400)


if __name__ == '__main__':
 app.run()

