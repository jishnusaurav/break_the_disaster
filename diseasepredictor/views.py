from __future__ import print_function
from django.shortcuts import render
import pandas as pd
import numpy as np
import os
from catboost import CatBoostRegressor, Pool
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
import time
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account




def Earthquake(request):
    if request.method == 'POST':        
        
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = None

        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)



        SAMPLE_SPREADSHEET_ID = '1S1bJ50odkAoNcTE6KJ60GMqcewQh1GBpIJtQPcUS4PE'


        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="Sheet1!A1:A5").execute()
        
        count=1
        data = []
        for i in result['values']:
            for j in i:
                data.append(int(j))
        data = np.array(
                    (data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],2,2,2,2,2,2,2,2,2
                    )
                ).reshape(1, 14)

        rand_forest=joblib.load("model.pkl")
        predictions = rand_forest.predict(data)
        x=str(predictions[0])
        print(predictions[0])
        print("123")
        return render(request,
                    'heart.html',
                    {
                        'context': x
                    })
    else:
        return render(request,
                  'heart.html',
                  {
                      'context': "No data"
                  })



def Tsunami(request):
    if request.method == 'POST':        
        
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = None

        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)



        SAMPLE_SPREADSHEET_ID = '1S1bJ50odkAoNcTE6KJ60GMqcewQh1GBpIJtQPcUS4PE'


        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="Sheet1!A1:A5").execute()
        
        count=1
        data = []
        for i in result['values']:
            for j in i:
                data.append(int(j))
        data = np.array(
                    (data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],2,2,2,2,2,2,2,2,2
                    )
                ).reshape(1, 14)

        rand_forest=joblib.load("model.pkl")
        predictions = rand_forest.predict(data)
        x=str(predictions[0])
        print(predictions[0])
        print("123")
        return render(request,
                    'tsunami.html',
                    {
                        'context': x
                    })
    else:
        return render(request,
                  'tsunami.html',
                  {
                      'context': "No data"
                  })



def Flood(request):
    
    if request.method == 'POST':  
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = None

        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)



        SAMPLE_SPREADSHEET_ID = '1S1bJ50odkAoNcTE6KJ60GMqcewQh1GBpIJtQPcUS4PE'


        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="Sheet1!A1:A5").execute()
        count=1
        data = []
        for i in result['values']:
            for j in i:
                data.append(int(j))     
        rand_forest=joblib.load("Flood.sav")
        predictions = rand_forest.predict([[data[0]]])
        if(predictions[0]>2):
            x="There is going to be a flood soon"
        else:
            x="There is no flood in the near future"
        
        print(predictions[0])
        print("123")

        return render(request,
                  'Flood.html',
                  {
                      'context': x
                  })
    else:
        return render(request,
                  'Flood.html',
                  {
                      'context': "No data"
                  })

def Drought(request):
    
    if request.method == 'POST':  
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = None

        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)



        SAMPLE_SPREADSHEET_ID = '1S1bJ50odkAoNcTE6KJ60GMqcewQh1GBpIJtQPcUS4PE'


        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="Sheet1!A1:A5").execute()
        count=1
        data = []
        for i in result['values']:
            for j in i:
                data.append(int(j))     
        rand_forest=joblib.load("Flood.sav")
        predictions = rand_forest.predict([[data[0]]])
        if(predictions[0]<2):
            x="There is going to be a drought soon"
        else:
            x="There is no drought in the near future"
        
        print(predictions[0])
        print("123")

        return render(request,
                  'Drought.html',
                  {
                      'context': x
                  })
    else:
        return render(request,
                  'Drought.html',
                  {
                      'context': "No data"
                  })
def home(request):

    return render(request,
                  'home.html')

# def handler404(request):
#     return render(request, '404.html', status=404)
