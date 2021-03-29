from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
@app.route("/")
def top():
    return render_template("index.html")

@app.route("/2")
def kyu():
    return render_template("kyu.html")

@app.route("/212345678")
def kyu_ko():
    k = request.args.get("kyuu")
    ji = request.args.get("jika")
    k2 = int(k)
    ji2 = int(ji)
    ko = k2 * ji2

    return render_template("kyu_ko.html",ko=ko)



@app.route("/3")
def en():
    return render_template("en.html")

if __name__ == "__main__":
    app.run(debug=True)
