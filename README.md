# A Simple Distraction-Free Page with your message

Use this application to display a focus-oriented message in a large format on your screen. Keep an important reminder or motivational quote visible while you work or when you are attempted to use your phone. 

# How to Run the Application

## Prerequisites

- Python 3.6 or higher
- Streamlit 1.34 or higher
- pymongo 4.7.3 or higher (optional)
 

## Installation

1. Clone the repository or download the `app.py` file.
2. Navigate to the directory where the file is saved.

## Install the required packages

```bash
pip install -r requirements.txt
```

## MongoDB Credentials 
1. The application uses MongoDB to store optionally the message and load it at app startup. This is however optional and you can safely skip this section. 
2. You can get a free MongoDB server at [MongoDB Atlas](https://cloud.mongodb.com)
3. Add the credentials of your mongodb instance to .streamlit/secrets.toml 
```
# .streamlit/secrets.toml
[mongo]
connection_string = mongodb+srv://<username>:<password>@hostname/?retryWrites=true&w=majority&appName=Cluster0
```


## Running the Application
Run the following command to start the Streamlit application:
```bash
streamlit run app.py
```

# Deploying the Application on Streamlit Cloud
1. Sign in to your [Streamlit Cloud](https://streamlit.io/cloud) account.
2. Click on "New app".
3. Connect your GitHub repository.
4. Optional: Provide the connection string to your MongDB instance
5.click "Deploy".
Your application will be deployed as a public app on Streamlit Cloud, allowing you to access it from your mobile phone for instance.

# Run the app as distraction-free on your phone
1. Install [Fully Kiosk Browser](https://play.google.com/store/apps/details?id=de.ozerov.fully&hl=en&pli=1) from Google Play Store 
2. Navigate to the settings and provide the URL of your app as defined in the previous step
3. Update your text message and Click on Save. The message is now displayed full screen on your phone.
4. Focus

# License
This project is licensed under the MIT License.