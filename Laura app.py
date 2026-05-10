import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Usamos el puerto que Render nos asigne, o el 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)