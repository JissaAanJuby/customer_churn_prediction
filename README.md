# Customer Churn Prediction App

This project is a machine learning application that predicts whether a telecom customer is likely to churn or stay, based on various customer service and account features. The app is built using Streamlit for the user interface and scikit-learn for the machine learning model.

## Features

- Trained Random Forest classifier on a telecom churn dataset
- 20+ input features including contract type, internet service, monthly charges, etc.
- Uses one-hot encoding and standard scaling for preprocessing
- Real-time predictions with a user-friendly web interface
- Model, scaler, and feature columns saved using `joblib`

## Files Included

- `streamlit_app.py`: Streamlit frontend for user interaction
- `churn_model.pkl`: Serialized model, scaler, and feature columns
- `churn_prediction.ipynb`: Jupyter notebook for data cleaning, preprocessing, and model training
- `requirements.txt`: Python dependencies for running the app
- `README.md`: Project documentation

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/churn-prediction-app.git
cd churn-prediction-app
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`.

## Project Workflow

1. Load and clean dataset (`WA_Fn-UseC_-Telco-Customer-Churn.csv`)
2. Perform feature engineering and encoding
3. Train a Random Forest Classifier
4. Save the model, scaler, and feature names
5. Build an interactive app using Streamlit
6. Deploy or run locally for real-time churn prediction

## License

This project is for educational and portfolio use. Contact the author for any commercial licensing or adaptation.

## Author

[Your Name]
