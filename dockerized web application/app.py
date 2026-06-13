from flask import Flask, render_template, jsonify
import socket
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
        hostname=socket.gethostname(),
        version=os.environ.get('APP_VERSION', '1.0.0'),
        env=os.environ.get('ENVIRONMENT', 'production')
    )

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'hostname': socket.gethostname(),
        'version': os.environ.get('APP_VERSION', '1.0.0')
    })

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'Dockerized Web Application',
        'author': 'CodTech Internship Project',
        'tech_stack': ['Python', 'Flask', 'Docker', 'Nginx'],
        'environment': os.environ.get('ENVIRONMENT', 'production'),
        'hostname': socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
