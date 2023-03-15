from flask import Flask, jsonify, request, render_template
import pickle
app = Flask(__name__)
# modal = pickle.load(open("d:\My_personal_files\Machine Learning\Linear Regression Whether Predictor WW2\webmodel\webmodel.pkl", "rb"))
class mdl:
    def predict(self,x):
        pdt = 1.0076005494236566*x + 1.0076005494236566
        return pdt
modal = mdl()
@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    x_predict = [float(x) for x in request.form.values()]
    x_predict = x_predict[0]
    prediction = modal.predict(x_predict)
    return render_template("index.html",prediction_text="The maximum tempreture is {}".format(prediction))

if __name__ == "__main__":
    
    app.run(debug=False,host='0.0.0.0')
    
