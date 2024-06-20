from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime
import streamlit as st

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def get_mongo_collection():
    if st.secrets.get("mongo") is None:
        print("No credentials to MongoDB provided in ./streamlit/secrets.toml")
        return None
    if st.secrets["mongo"].get("connection_string") is None:
        print("No connection string to MongoDB provided, use connection_string")
        return None
    connection_string = st.secrets["mongo"]["connection_string"]
    try:
        print(f"connecting to MongoDB at {connection_string} ")
        client = MongoClient(connection_string)
        db = client["distraction-free-db"] # The whole app uses this database
        collection = db.messages  # Messages are stored in a  collection called 'messages'
        return collection
    except ConnectionFailure as e:
        print (e)
        return None


# Function to save the text to MongoDB DB
def save_text(collection, msg_text):
    if collection is None:
        print("Connection to MongoDB is not available while saving the text")
        return False
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = {
        "msg": msg_text,
        "timestamp": current_time
    }
    collection.insert_one(message)
    return True

# Function to retrieve the last saved text from MongoDB
def load_last_text(collection):
    if collection is None:
        print("Connection to MongoDB is not available while loading last text")
        return None
    try:
        last_message = collection.find_one(sort=[('_id', -1)])  # Get the latest document based on _id
        if last_message:
            return last_message['msg']
        print("No message retrieved from MongoDB")
        return ""
    except Exception as e:
        print(e)
        return ""