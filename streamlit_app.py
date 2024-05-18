import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title='Social Network Ad Purchase Prediction', layout='wide')

# Title and description
st.title('Social Network Ad Purchase Prediction')
st.markdown('''
This application predicts whether a user will purchase a product from a social network advertisement based on their gender, age, and estimated salary.

### Instructions:
1. Select the gender (1 for Male, 0 for Female).
2. Adjust the sliders to set the user's age and estimated salary.
3. Click on the **Predict** button to see the result.
''')

# Input features
st.sidebar.header('User Input Features')
gender = st.sidebar.radio('Gender (1 for Male, 0 for Female)', [0, 1])
age = st.sidebar.slider('Age', 1, 80, 30)
salary = st.sidebar.slider('Estimated Salary', 1000, 200000, 10000)

# URL to your deployed Flask API
url = 'https://social-media-ad-purchase.onrender.com/predict'

if st.sidebar.button('Predict'):
    response = requests.post(url, json={'gender': gender, 'age': age, 'salary': salary})
    if response.status_code == 200:
        prediction = response.json().get('prediction')
        if prediction is not None:
            result = "True" if prediction == "True" else "False"
            st.sidebar.success(f'This user will buy from social network advertisement: {result}')
        else:
            st.sidebar.error('Invalid response from the server.')
    else:
        st.sidebar.error('Failed to get prediction')

# Footer with link to deployed Flask app
st.markdown('''
---
Flask - Code available at [GitHub](https://github.com/kushalmatalia/Social_Media_Ad_Purchase)
            
Streamlit - Code available at [GitHub](https://github.com/kushalmatalia/Social_Media_Ad_Purchase_)
''')
