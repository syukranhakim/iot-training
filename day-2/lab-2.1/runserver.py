from flask import Flask, request, render_template, jsonify
import csv

app = Flask(__name__)

csv_file = 'log.csv'


@app.get("/")
def hello():
    return "Hello World"


@app.get("/data")
def get_data():

    rows = []
    with open(csv_file, newline="") as fcsv:
        reader = csv.reader(fcsv)
        for row in reader:
            rows.append(float(row[0]))

    print(rows)

    return render_template("data.html", data=rows)


@app.post("/push-data")
def post_data():
    data = request.json
    #print(data)

    temp = data.get('temperature')

    if temp is None:
        return jsonify({"status": "error"}), 400


    with open(csv_file, 'a', newline='') as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow([temp])

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
