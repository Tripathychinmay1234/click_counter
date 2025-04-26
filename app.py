from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

counter_file = "counter.txt"

def read_counter():
    try:
        with open(counter_file, "r") as f:
            return int(f.read())
    except:
        return 0

def write_counter(count):
    with open(counter_file, "w") as f:
        f.write(str(count))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_count")
def get_count():
    count = read_counter()
    return jsonify({"count": count})

@app.route("/increment", methods=["POST"])
def increment():
    count = read_counter() + 1
    write_counter(count)
    return jsonify({"count": count})

if __name__ == "__main__":
    app.run(debug=True)
