from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from prometheus_client import Counter, Histogram, generate_latest, Gauge, Summary
import time
import os
import psutil
import random
import threading

# Initialize Flask app
app = Flask(__name__)
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
http_duration = Histogram('flask_app_request_duration_seconds', 'Histogram of HTTP request durations in seconds', buckets=[0.1, 0.5, 1, 2, 5])
error_counter = Counter('flask_app_http_errors_total', 'Total HTTP errors', ['method', 'endpoint', 'status_code'])
response_size = Histogram('flask_app_response_size_bytes', 'Size of HTTP responses in bytes', buckets=[100, 500, 1000, 5000, 10000])


# 🖥️ System Metrics (CPU, Memory, Disk, Network, Threads)
cpu_usage = Gauge('flask_cpu_usage_percent', 'CPU usage percentage')
memory_usage = Gauge('flask_memory_usage_percent', 'Memory usage percentage')
disk_usage = Gauge('flask_disk_usage_percent', 'Disk usage percentage')
network_sent = Gauge('flask_network_bytes_sent', 'Total network bytes sent')
network_received = Gauge('flask_network_bytes_received', 'Total network bytes received')
thread_count = Gauge('flask_thread_count', 'Number of active threads')
process_count = Gauge('flask_process_count', 'Number of running processes')
uptime = Gauge('flask_uptime_seconds', 'Server uptime in seconds')


# 👤 User Metrics
active_users = Gauge('flask_active_users', 'Number of active users')
# active_sessions = Gauge('flask_active_sessions', 'Number of active user sessions')


# 💾 Database Query Metrics
db_query_time = Summary('flask_db_query_duration_seconds', 'Time taken for database queries')


# 📊 Update System Metrics
def update_system_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage('/').percent)
    network_sent.set(psutil.net_io_counters().bytes_sent)
    network_received.set(psutil.net_io_counters().bytes_recv())
    thread_count.set(threading.active_count())
    process_count.set(len(psutil.pids()))
    uptime.set(time.time() - start_time)




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
    http_duration.observe(duration)
    response_size.observe(len(response.data))  # Track response size
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
    start_time = time.time()
    with app.app_context():
        db.create_all()  # Create all tables defined by the models
        add_predefined_data()  # Add predefined features if not already present
    """Route to handle features - fetch and add"""
    if request.method == 'GET':
        features = Feature.query.all()
        db_query_time.observe(time.time() - start_time)
        return jsonify([{'id': f.id, 'title': f.title, 'description': f.description} for f in features])
    
    elif request.method == 'POST':
        data = request.json
        new_feature = Feature(title=data['title'], description=data['description'])
        db.session.add(new_feature)
        db.session.commit()
        db_query_time.observe(time.time() - start_time)
        return jsonify({'message': 'Feature added successfully'}), 201
    

# Test route to verify server is running
# 📌 API Route: Home
@app.route('/', methods=['GET'])
def home():
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
    start_time = time.time() 
    app.run(host='0.0.0.0', port=5000)
