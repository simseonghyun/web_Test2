from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    print("Ddd")
    return render_template('home.html')


@app.route("/test", methods = ['GET', 'POST'])
def test():
    print("나 실행되냐?")
    return render_template('home2.html')



if __name__ == '__main__':
    app.run(debug=True)
