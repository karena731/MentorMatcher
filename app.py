from flask import Flask, render_template, request
import logging

app = Flask(__name__,
        static_url_path='',
        static_folder='static',
        template_folder='templates')

@app.route("/", methods=["GET"])
def index():
    """Homepage"""
    return render_template('index.html', title='Mentor Matcher')
    #return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
