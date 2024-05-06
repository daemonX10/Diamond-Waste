from flask import Flask,request,render_template,jsonify
from src.pipelines.predication_pipeline import PredictPipeline,CustomData

application=Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
