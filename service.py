from flask import Flask, render_template, request, session, flash, redirect,  url_for, jsonify, make_response

app = Flask(__name__)
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, threaded=True)
