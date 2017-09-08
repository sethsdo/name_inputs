from flask import Flask, render_template, request, redirect
app = Flask(__name__)

dev = True

@app.route('/')
def my_portfolio():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create_user():
    print "Got user info"
    name = request.form['name']
    print name
    return redirect('/')

app.run(debug=dev)

