from flask import Flask, render_template
from database import load_jobs

app = Flask(__name__, static_url_path='/static')

@app.route('/')

def index():
    jobs = load_jobs()
    return render_template('index.html', jobs = jobs)

if __name__ == "__main__":
    app.run(debug=True)


