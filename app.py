from flask import Flask
from keras.models import load_model
from flask import render_template
from flask import request

app = Flask("diabetes_app")

model = load_model("diabetes_model.h5")



@app.route("/diabetes", methods=['GET'])
def dia():

  preg_no = int(request.args.get('p'))

  glucose = int(request.args.get('pg'))

  bp = int(request.args.get('bp'))

  thickness = int(request.args.get('sft'))

  insulin = int(request.args.get('in'))

  body_mass = float(request.args.get('bm'))

  pedigree_fn = float(request.args.get('pf'))

  age = int(request.args.get('ag'))

  prediction = model.predict([[ preg_no,glucose,bp,thickness,insulin,body_mass,pedigree_fn,age ]])

  output = round(prediction[0][0])


  if output == 1:
    return render_template("diaPositive.html")

  elif output == 0:
    return render_template("diaNegative.html")

@app.route("/home", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/", methods=['GET'])
def index():
  return render_template("index.html")


app.run(host="0.0.0.0", port=5000)
