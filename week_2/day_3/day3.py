
from  flask import Flask,render_template


app= Flask(__name__)

@app.route('/')
def home():
    response="hello"
    return render_template('index.html',result=response)

@app.route('/Chatbot')
def chat():
    return"<h2> chatbot</h2>"

app.run(debug=True)


