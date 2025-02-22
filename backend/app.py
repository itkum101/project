from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from prometheus_client import Counter, Histogram, generate_latest, Gauge, Summary
import time
import os
import psutil
import random
import threading
from prometheus_flask_exporter import PrometheusMetrics

# Initialize Flask app
app = Flask(__name__)
metrics = PrometheusMetrics(app)
CORS(app)  # Enable Cross-Origin Resource Sharing


##START SQL
# Read environment variables for database configuration
mysql_host = os.getenv('MYSQL_HOST', 'db')
mysql_port = os.getenv('MYSQL_PORT', '3306')
mysql_user = os.getenv('MYSQL_USER', 'user')
mysql_password = os.getenv('MYSQL_PASSWORD')  # Ensure this is set in the environment
mysql_database = os.getenv('MYSQL_DATABASE', 'myapp')

# Ensure the MYSQL_PASSWORD is provided
if not mysql_password:
    raise ValueError("MYSQL_PASSWORD environment variable is required.")
print(f'MYSQL_PASSWORD is: {mysql_password}')

# Configure the MySQL database using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


### END SQL


# 🚀 API Monitoring Metrics
page_views = Counter('flask_app_page_views', 'Total page views')
http_requests = Counter('flask_app_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status_code'])









# Database Model for Feature
class Feature(db.Model):
    """Feature Model for storing features"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feature {self.title}>'

# Track HTTP request duration and count
@app.before_request
def track_request():
    request.start_time = time.time()

@app.after_request
def count_request(response):
    duration = time.time() - request.start_time
    # http_duration.observe(duration)
    # response_size.observe(len(response.data))  # Track response size
    http_requests.labels(method=request.method, endpoint=request.path, status_code=response.status_code).inc()

    if response.status_code >= 400:
        error_counter.labels(method=request.method, endpoint=request.path, status_code=response.status_code).inc()

    return response

@app.route('/metrics', methods=['GET'])
def metrics():
    page_views.inc()  # Increment page views counter
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}


# Route for handling features - fetch and add
@app.route('/features', methods=['GET', 'POST'])
def features():
    page_views.inc() 
    with app.app_context():
        db.create_all()  # Create all tables defined by the models
        add_predefined_data()  # Add predefined features if not already present
    """Route to handle features - fetch and add"""
    if request.method == 'GET':
        features = Feature.query.all()
        return jsonify([{'id': f.id, 'title': f.title, 'description': f.description} for f in features])
    
    elif request.method == 'POST':
        data = request.json
        new_feature = Feature(title=data['title'], description=data['description'])
        db.session.add(new_feature)
        db.session.commit()
        return jsonify({'message': 'Feature added successfully'}), 201
    

# Test route to verify server is running
# 📌 API Route: Home
@app.route('/', methods=['GET'])
def home():
    page_views.inc() 
    return "Flask server is running with advanced Prometheus metrics!"



# Adding predefined features to the database if they don't exist
def add_predefined_data():
    """Predefine features if not already in the database"""
    
    # Predefined features
    predefined_features = [
        {"title": "Decentralized Inference", "description": "Run large language models across multiple peers, enabling distributed and efficient computation."},
        {"title": "WebGPU Integration", "description": "Leverage the power of modern GPUs directly from your browser for accelerated AI processing."},
        {"title": "Scalable Architecture", "description": "Scale effortlessly across devices with fault tolerance and dynamic node allocation."},
        {"title": "Enhanced Privacy", "description": "Keep sensitive data on your local device while contributing to decentralized AI computations."}
    ]
    
    for feature in predefined_features:
        if not Feature.query.filter_by(title=feature['title']).first():
            new_feature = Feature(title=feature['title'], description=feature['description'])
            db.session.add(new_feature)
    
    db.session.commit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
