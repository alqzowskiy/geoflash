from flask import Flask, render_template, url_for, json
import gunicorn
app = Flask(__name__)

@app.route('/')
def index():
    with open('static/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)