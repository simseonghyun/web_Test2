from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    testData = "sim"
    return render_template('home.html',testDataHtml = testData)


if __name__ == '__main__':
    app.run(debug=True)
