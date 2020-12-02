from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        print("We received GET")
        return render_template('kontakt.html')
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return render_template('kontakt.html')


@app.route("/mypage/me", methods=['GET'])
def me():
    print("We received GET")
    return render_template('index.html')
