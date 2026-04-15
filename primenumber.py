from flask import Flask, request
import json
app = Flask(__name__)
@app.route("/prime_number/<number>/")
def prime_number(number):
    o=[]
    numberr=int(number)
    for i in range(1,numberr+1):
        if numberr%i==0:
            e = str(i)
            o.append(e)
    if len(o) == 2:
        return json.dumps({
            "number":number,
            "prime":"True",
            })
    else:
        return json.dumps({
            "number": number,
            "prime": "False",
        })
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000)