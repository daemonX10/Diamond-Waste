from flask import Flask,request,render_template,jsonify
from src.pipelines.predication_pipeline import PredictPipeline,CustomData

application=Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict():
    if request.method== 'GET':
        return render_template('form.html')
    
    else:
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        
        print(data.get_data_as_dataframe())
        
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        
        results = round(pred[0],2)
        print(results)
        
        return render_template('form.html',  prediction_text = 'Predicted Price: $ {}'.format(results))

if __name__=='__main__':
    print("Server is running at port 3000")
    print("link:",'http://localhost:3000/')
    app.run(host='0.0.0.0',port=3000,debug=True)
    
    
   