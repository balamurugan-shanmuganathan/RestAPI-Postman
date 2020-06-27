import pickle
import numpy as np
import pandas as pd

class predObj:
    def predict_log(self, dict_pred):
        # Load Scaler pickle file
        with open("standardScalar.sav", 'rb') as f:
            scalar = pickle.load(f)
        # Load Model Pickle file
        with open("modelForPrediction.sav", 'rb') as f:
            model = pickle.load(f)
        
        data_df = pd.DataFrame(dict_pred,index=[1,])
        scaled_data = scalar.transform(data_df)
        predict = model.predict(scaled_data)
        if predict[0] ==1 :
            result = 'Patiant is Diabetic'
        else:
            result ='Patiant is Non-Diabetic'
        return result
