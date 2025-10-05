from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil nilai dari form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Prediksi
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Perkiraan harga rumah: {output}')

if __name__ == "__main__":
    app.run(debug=True)
