import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "CyberDyne Logistics API is running securely."})

@app.route('/process', methods=['POST'])
def process_data():
    try:
        # Get raw data from request
        raw_data = request.data
        
        # FIX: Replaced unsafe pickle.loads() with secure json.loads()
        # This prevents arbitrary code execution vulnerabilities.
        data = json.loads(raw_data.decode('utf-8'))
        
        # Process the parsed JSON data
        response_data = {
            "status": "success",
            "message": "Data processed securely",
            "received_data": data
        }
        return jsonify(response_data), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)