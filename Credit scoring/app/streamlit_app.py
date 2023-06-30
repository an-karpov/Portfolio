import streamlit as st
from PIL import Image
import pickle
import sklearn
from sklearn.pipeline import Pipeline
import pandas as pd
import os

st.title('Credit Score Classification')
st.caption('Made by Andrey Karpov')

st.markdown('''
            [GitHub repository](https://github.com/an-karpov/Portfolio/tree/main/Credit%20scoring).

            The presented model decides whether to give you a credit or not.

            You can play with parameters and check yourself ;)
''')


# default parameters
RevolvingUtilizationOfUnsecuredLines = 0.2
NumberOfDependents = 1
DebtRatio:float = 0.5
age = 30
NumberOfTime30_59 = 0
NumberOfTime60_89DaysPastDueNotWorse = 0
NumberOfTimes90DaysLate = 0
MonthlyIncome = 3000.0
NumberOfOpenCreditLinesAndLoans = 6

# model
with open('./models/xgb_pipeline.pickle', 'rb') as f:
    model = pickle.load(f)

profile = st.radio('Choose a profile:', options=['Ivan', 'Tolya', 'Andrey'], horizontal=True)

if profile == 'Ivan':
    RevolvingUtilizationOfUnsecuredLines = 0.8
    NumberOfDependents = 5
    DebtRatio = 100.0
    age = 40
    NumberOfTime30_59 = 10
    NumberOfTime60_89DaysPastDueNotWorse = 10
    NumberOfTimes90DaysLate = 10
    MonthlyIncome = 1000.0
    NumberOfOpenCreditLinesAndLoans = 10
elif profile == 'Tolya':
    RevolvingUtilizationOfUnsecuredLines = 0.5
    NumberOfDependents = 2
    DebtRatio = 1.0
    age = 25
    NumberOfTime30_59 = 2
    NumberOfTime60_89DaysPastDueNotWorse = 0
    NumberOfTimes90DaysLate = 0.0
    MonthlyIncome = 3000.0
    NumberOfOpenCreditLinesAndLoans = 2
elif profile == 'Andrey':
    RevolvingUtilizationOfUnsecuredLines = 0.2
    NumberOfDependents = 4
    DebtRatio = 0.5
    age = 35
    NumberOfTime30_59 = 0
    NumberOfTime60_89DaysPastDueNotWorse = 0
    NumberOfTimes90DaysLate = 0
    MonthlyIncome = 10000.0
    NumberOfOpenCreditLinesAndLoans = 4

with st.sidebar:
    st.header('Choise your parameters')

    age = st.slider('What is your age?', min_value=18, max_value=100, step=1, value=age)

    monthly_income = st.number_input('What is your Monthly Income?', min_value=0.0, max_value=30000.0, value=MonthlyIncome)

    depedents = st.number_input('How many dependents do you have?', min_value=0, max_value=20, step=1, value=NumberOfDependents)

    number_of_credits = st.number_input('How many number of open credit lines and loans do you have?', min_value=0, max_value=100, step=1, value=NumberOfOpenCreditLinesAndLoans)

    dept_ratio = st.number_input('Your dept ratio:', min_value=0.0, max_value=3000.0, step=0.01, value=DebtRatio)
    # dept_ratio = st.slider('Your dept ratio:', min_value=0.0, max_value=3000.0, step=0.01, value=DebtRatio)

    rev_util = st.slider('Total balance on credit cards and personal lines of credit (RevolvingUtilizationOfUnsecuredLines):', min_value=0.00, max_value=1.00, step=0.01, value=RevolvingUtilizationOfUnsecuredLines)

    number_of_time_30_59 = st.number_input('How many times in the last 2 years there has been a delay of 30-59 days?', min_value=0, max_value=100, step=1, value=NumberOfTime30_59)

    number_of_time_60_89 = st.number_input('How many times in the last 2 years there has been a delay of 60-89 days?', min_value=0, max_value=100, step=1, value=NumberOfTime60_89DaysPastDueNotWorse)

    number_of_time_90 = st.number_input('How many times there was a delay (90 days or more)?', min_value=0, max_value=100, step=1, value=NumberOfTime60_89DaysPastDueNotWorse)

    run = st.button( 'Run!')

st.header('Results: ')
placeholder=st.empty()
if run:
    resp = {
        'RevolvingUtilizationOfUnsecuredLines': [rev_util],
        'NumberOfTime30-59DaysPastDueNotWorse': [number_of_time_30_59], 
        'NumberOfDependents': [depedents],
        'DebtRatio': [dept_ratio], 
        'NumberOfTime60-89DaysPastDueNotWorse': [number_of_time_60_89], 
        'age': [age],
        'NumberOfTimes90DaysLate': [number_of_time_90], 
        'MonthlyIncome': [monthly_income],
        'NumberOfOpenCreditLinesAndLoans': [number_of_credits]
    }

    data = pd.DataFrame.from_dict(resp)
    is_rejected = model.predict(data)[0]

    if is_rejected:
        # t1 = plt.Polygon([[5, 0.5], [5.5, 0], [4.5, 0]], color='black')
        placeholder.markdown('Credit is not approved :\\')
        image = Image.open('./pics/decline.png')
        st.image(image, width=300)
    else:
        st.balloons()
        placeholder.markdown('Credit **approved**. Congratulations!!!')
        image = Image.open('./pics/approved.png')
        st.image(image, width=300)
