from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Read environment variables for database configuration
mysql_host = os.getenv('MYSQL_HOST', 'mysql-service')
mysql_port = os.getenv('MYSQL_PORT', '3306')
mysql_user = os.getenv('MYSQL_USER', 'user')
mysql_password = os.getenv('MYSQL_PASSWORD', 'userpassword')
mysql_database = os.getenv('MYSQL_DATABASE', 'myapp')

# Configure the MySQL database using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Model for Feature
class Feature(db.Model):
    """Feature Model for storing features"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feature {self.title}>'

# Route for handling features - fetch and add
@app.route('/features', methods=['GET', 'POST'])
def features():
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

@app.route('/', methods=['GET'])
def start():
    """Run this first"""
    with app.app_context():
        db.create_all()  # Create all tables defined by the models
        add_predefined_data()  # Add predefined features if not already present
    return jsonify({'message': "Initialized all parameters"}), 200

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

# Main function to run the app
if __name__ == '__main__':
    # Create database tables if they don't exist and add predefined features
    with app.app_context():
        db.create_all()  # Create all tables defined by the models
        add_predefined_data()  # Add predefined features if not already present
    
    # Run the app
    app.run(host='0.0.0.0', port=5000)
