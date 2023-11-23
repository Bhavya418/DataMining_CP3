#import library
import uvicorn
from fastapi import FastAPI
from DataModel import WinnerData
import numpy as np
import pickle
import pandas as pd

#create the app object
app=FastAPI()
pickle_model=open("notebooks/winner_prediction.pkl","rb")
classifier=pickle.load(pickle_model)

#default route
@app.get('/')
def index():
    return{"message":"Hello IDM Students"}

#default route
@app.get('/api-demo')
def index():
    return{"message":"This is demo API"}

#Prediction Function, return the predicted result in JSON
@app.post('/predict')
def predict(data:WinnerData):
    #convert data obj to dictionary
    icc_ranking = {
        'India': 1,
        'Australia': 2,
        'Pakistan': 3,
        'South Africa': 4,
        'New Zealand': 5,
        'England': 6,
        'Sri Lanka': 7,
        'Bangladesh': 8,
        'Afghanistan': 9,
        'Netherlands': 10, 
    }
    teams_final = pd.read_csv('notebooks/teams_final.csv')
    teams_final=teams_final.drop(teams_final.columns[0], axis=1)
    # print(teams_final)
    data=dict(data)
    team1=data['team1']
    team2=data['team2']
    ranking1 = icc_ranking[team1]
    ranking2 = icc_ranking[team2]
    data = {
        'Team_1': [team1],
        'Team_2': [team2],
        "Team_1_Position": [ranking1],
        "Team_2_Position": [ranking2]
    }
    df_temp = pd.DataFrame(data)
    
    prediction_set = pd.get_dummies(df_temp, prefix=['Team_1', 'Team_2'], columns=['Team_1', 'Team_2'])
    notPresentColumns = set(teams_final.columns) - set(prediction_set.columns)
    
    for c in notPresentColumns:
        prediction_set[c] = 0
    prediction_set = prediction_set[teams_final.columns]

    prediction_set = prediction_set.drop(['Winner'], axis=1)
    print(prediction_set)
    pred = classifier.predict(prediction_set)
    print(pred)
    # prediction = classifier.predict(prediction_set)
    # print(prediction)

    # #return probability
    # if(prediction[0]>0.5):
    #     prediction="Fake note"
    # else:
    #     prediction="Its a Bank note"
    return {
        'prediction': pred[0]
    }

#Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    

#Command to run API server   
#python -m uvicorn main:app --reload