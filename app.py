from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    form_values = []
    for value in request.form.values():
        if value.lower() == 'yes':
            form_values.append(1.0)
        elif value.lower() == 'no':
            form_values.append(0.0)
        elif value.lower() == 'furnished':
            form_values.extend([1.0, 0.0])
        elif value.lower() == 'semi-furnished':
            form_values.extend([0.0, 1.0])
        elif value.lower() == 'unfurnished':
            form_values.extend([0.0, 0.0])
        else:
            form_values.append(float(value))

    final_features = [form_values]
    prediction = model.predict(final_features)
    
    # konversi prediksi ke rupiah dan ubah ke format lokal
    hasil_rupiah = float(prediction[0]) * 100  
    formatted_harga = f"{hasil_rupiah:,.0f}".replace(",", ".")
    
    return render_template('index.html', prediction_text=f'Perkiraan harga rumah: Rp {formatted_harga}')


if __name__ == "__main__":
    app.run(debug=True)
