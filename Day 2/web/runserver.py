from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello World"


@app.get("/data")
def get_data():
    return render_template("index.html")


@app.post("/data")
def post_data():
    data = request.json
    print(data)
    return "OK"


if __name__ == "__main__":
    app.run()
