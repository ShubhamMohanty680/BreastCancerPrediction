from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from sklearn.datasets import load_breast_cancer

uri = "mongodb+srv://shubham:Shubham@cluster0.oev8htd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME='ML_Project'
COLLECTION_NAME='breast_cancer'

# read data as an dataframe
breast_cancer_data=load_breast_cancer()

#convert the data into dataframe
df=pd.DataFrame(data=breast_cancer_data.data,columns=breast_cancer_data.feature_names) 

#add the target column to the DataFrame
df['target'] = breast_cancer_data.target



#convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)