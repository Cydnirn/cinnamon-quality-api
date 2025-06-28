from flask import Flask, request, jsonify

from model.inference import create_custom_sample, predict_cinnamon_quality

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "healthy", "message": "Cinnamon quality prediction API is running"})

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint to predict cinnamon quality based on input parameters"""
    try:
        data = request.get_json()

        # Extract parameters from request
        moisture = data.get('moisture')
        ash = data.get('ash')
        oil = data.get('volatile_oil')
        acid = data.get('acid_insoluble_ash')
        chromium = data.get('chromium')
        coumarin = data.get('coumarin')

        # Create sample and get prediction
        sample = create_custom_sample(moisture, ash, oil, acid, chromium, coumarin)
        prediction = predict_cinnamon_quality(sample)

        return jsonify({"prediction": str(prediction[0]), "confidence": str(prediction[1]), "status": "success"})
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
