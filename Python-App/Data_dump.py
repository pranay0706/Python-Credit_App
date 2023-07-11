import pymongo
import pandas as pd
import json
from typing import List
import certifi

#Provide the MongoDB Localhost URL to Connect Python to MongoDB.
ca = certifi.where()
client= pymongo.MongoClient("mongodb+srv://<user-name>:<password>@<cluster-name>.tlhouhq.mongodb.net/test", tlsCAFile=ca)

DATA_FILE_PATH="D:\DevOps\Credit-Card\CreditCard.csv"
DATABASE_NAME="CreditCard"
COLLECTION_NAME="Default"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert Dataframe to json format to dump this records into mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.to_json(orient='records')))
    print(json_record[0])

    #Insert Converted json Record To MongoDB Database
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
