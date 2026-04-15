from flask import Flask, request
import json

app = Flask(__name__)

airports = {
    "LFLL": {
        "name": "Lyon Saint-Exupery Airport",
        "city": "Lyon",
        "country": "FR"
    }
}

@app.route("/airport/<ICAO_code>")
def get_airport(ICAO_code):
    ICAO_code = ICAO_code.upper()

    if ICAO_code in airports:
        data = airports[ICAO_code]

        return json.dumps({
            "icao": ICAO_code,
            "name": data["name"],
            "city": data["city"],
            "country": data["country"]
        })
    else:
        return json.dumps({
            "error": "a 404 error occured"
        })


if __name__ == "__main__":
    app.run(host="127.0.1.1", port=5001)