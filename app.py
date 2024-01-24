from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = 'gemini-pro'

# [theme]
# primaryColor = "#F63366"
# backgroundColor = "#FFFFFF"
# secondaryBackgroundColor = "#F0F2F7"
# textColor = "#262730"
# font = "monospace"

with st.sidebar:
    st.title("The Quizmaster!")
    st.write("Embark on a knowledge-packed journey with QuizMaster, your go-to app for exploring diverse topics. Whether you're a trivia enthusiast or a casual learner, QuizMaster caters to all levels of curiosity. ")
    st.write("Dive into engaging questions that not only test your knowledge but also provide insightful explanations, turning every answer—right or wrong—into a learning opportunity. Challenge yourself solo or compete with friends to see who emerges as the ultimate QuizMaster. It's time to make learning fun, accessible, and rewarding. Use QuizMaster now and unlock a world of information at your fingertips!")

# Call the model and print the response.
st.title("The Quizmaster!")
nq = ["MCQ","One Word Answer","Short Answer","Long Answer"]

col1, col2 = st.columns(2)
with col1:
    sub = st.text_input('Subject')
    top = st.text_input('Topic in Subject')
    typ = st.selectbox('Type of questions',options=nq)
    
with col2:
    question_no = st.selectbox('Number of Questions',options=['1','2','3','4','5'])
    exp = st.selectbox('Explanation Required',['Yes','No'])
    level =st.selectbox('Level of Complexity',['Very Easy','Easy','Medium','Hard','Very Hard!'])

prompt = 'You are a college professor in '+sub+'. You specialise in '+top+'.' 
prompt += 'Create '+question_no+' ' +typ+' questions based on the topic of '+top+'. ' 
prompt += 'The level of complexity of the questions should be  '+level+'. ' 
prompt += 'After each question wait for my answer and explain my answer.' 
prompt += exp+' ,explanation is required after every answer.'

a = st.button('Generate')
if a:
    with st.spinner('Wait for it'):
        gemini = genai.GenerativeModel(model_name=model)
        response = gemini.generate_content(prompt,stream=False)
        st.text_area(label ="",value=response.text,height=500)
    st.success('Done')
