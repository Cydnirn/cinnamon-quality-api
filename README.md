# Cinnamon Quality Prediction Model

This project provides a machine learning model that predicts cinnamon quality based on various physical and chemical properties. The model is exposed through a simple Flask API, which can be run locally or deployed using Docker.

Data from [Kaggle](https://www.kaggle.com/datasets/madaraweerasingha/cinnamon-quality-classification)

## Project Overview

The Cinnamon Quality Prediction Model analyzes the following parameters to determine cinnamon quality:
- Moisture content (%)
- Ash content (%)
- Volatile oil content (%)
- Acid-insoluble ash (%)
- Chromium content (mg/kg)
- Coumarin content (mg/kg)

Put the model pickle file inside the model directory.

## Installation and Setup

### Prerequisites

- Python 3.8+ (3.9 recommended for best compatibility)
- pip (Python package installer)
- Docker (optional, for containerized deployment)

### Local Setup with Python

1. Clone the repository:
```bash
git clone <repository-url>
cd cinnamon-model
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the API:
```bash
python app.py
```

The API will be available at http://localhost:5000/

### Building and Running with Docker

1. Build the Docker image:
```bash
docker build -t cinnamon-quality-api .
```

2. Run the Docker container:
```bash
docker run -p 5000:5000 cinnamon-quality-api
```

The API will be available at http://localhost:5000/

## API Usage

### Endpoints

- **POST /predict**: Predict cinnamon quality based on input parameters.

### Request Format

The request should be a JSON object with the following structure:
```json
{
  "moisture": <float>,
  "ash": <float>,
  "volatile_oil": <float>,
  "acid_insoluble_ash": <float>,
  "chromium": <float>,
  "coumarin": <float>
}
```

### Response Format

The response will be a JSON object with the predicted quality score:
```json
{
  "prediction": "Medium" | "High" | "Low",
  "confidence": <float>,
  "status": "success"
}
```

### Example Request

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"moisture": 12.171229, "ash": 6.843436,
"volatile_oil": 0.776597,
"acid_insoluble_ash": 0.439549,
"chromium": 0.003525,
"coumarin": 0.007177}'
```

### Example Response

```json
{
  "prediction": "Medium",
  "confidence": 100.00,
  "status": "success"
}
```
