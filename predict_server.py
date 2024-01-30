from flask import Flask, render_template, jsonify, request
from tensorflow.data import Dataset
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import TextVectorization
import pickle

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.secret_key = 'B;}}S5Cx@->^^"hQT{T,GJ@YI*><17'

labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]


def prediction(comment):
    model = load_model("toxicity.h5")

    from_disk = pickle.load(open("tv_layer.pkl", "rb"))
    vectorizer = TextVectorization.from_config(from_disk['config'])
    vectorizer.adapt(Dataset.from_tensor_slices(["xyz"]))
    vectorizer.set_weights(from_disk['weights'])

    vectorized = vectorizer([comment])
    predicted = model.predict(vectorized)
    labels_strings = []
    for index, label in enumerate(labels):
        if predicted[0][index] > 0.5:
          labels_strings.append(label.capitalize())
          #result += f"{label}: {predicted[0][index] > 0.5} \n"

    if len(labels_strings) == 0:
        return "Nothing toxic here!"

    return ", ".join(labels_strings)

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        result = prediction(request.form['text'])
        response = jsonify({'result': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status_code = 200
        return response
    if request.method == 'GET':
        return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=False, host='localhost', port=5000)