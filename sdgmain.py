import streamlit as st
import requests
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pytrends.request import TrendReq
from streamlit_lottie import st_lottie

pytrend = TrendReq()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets9.lottiefiles.com/datafiles/dc49lw7cOTLEo6y/data.json"
lottie_json = load_lottieurl(lottie_url)




st.title('United Nations Sustainable Development Goals Interactive Questionnaire')

st_lottie(lottie_json, key="1")




#Be able to see the associated keywoards for the SDG

#use pytrends

#Be able to visualize the trends of those keywords

#Populate graph based on choice

#Maybe add locations where it is popular too
######################################################################################################################################################

st.markdown("<h1 style='text-align: center; color: black;'>No Poverty</h1>", unsafe_allow_html=True)
with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Globally, the number of people living in extreme poverty declined from 36 per cent in 1990 to 10 per cent in 2015. But the pace of change is decelerating and the COVID-19 crisis risks reversing decades of progress in the fight against poverty. New research published by the UNU World Institute for Development Economics Research warns that the economic fallout from the global pandemic could increase global poverty by as much as half a billion people, or 8% of the total human population. This would be the first time that poverty has increased globally in thirty years, since 1990.") 
    st.text("")
    st.write("More than 700 million people, or 10 per cent of the world population, still live in extreme poverty today, struggling to fulfil the most basic needs like health, education, and access to water and sanitation, to name a few. The majority of people living on less than $1.90 a day live in sub-Saharan Africa. Worldwide, the poverty rate in rural areas is 17.2 per cent—more than three times higher than in urban areas.")  
    st.text("")
    st.write(
    "For those who work, having a job does not guarantee a decent living. In fact, 8 per cent of employed workers and their families worldwide lived in extreme poverty in 2018. One out of five children live in extreme poverty. Ensuring social protection for all children and other vulnerable groups is critical to reduce poverty.")

    st.text("")
    agree = st.checkbox('Would you like to view the general trend of interest in this topic worldwide')
    if agree:
        with st.spinner('Wait for it...'):
            pytrend.build_payload(kw_list=['Poverty'])
            rq = pytrend.related_queries()
            rq.values()
            st.write(rq.get('Poverty').get('top'))

st.text("")
with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-01_resized.jpg", width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal1/")
st.text("")
q1 = st.slider('How personal is this to you?', 0, 5, key="1")



 ###################################################################################################################################################################       


st.header('Zero Hunger')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-02_resized.jpg")
q2 = st.slider('How personal is this to you?', 0, 5, key="2")
op2 = pytrend.build_payload(kw_list=["Hunger"])
st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

st.header('Good Health and Well-being')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-03_resized.jpg")
q3 = st.slider('How personal is this to you?', 0, 5, key="3")
op3 = pytrend.build_payload(kw_list=["Good Health"])
st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

st.header('Quality Education')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-04_resized.jpg")
q4 = st.slider('How personal is this to you?', 0, 5, key="4")
op4 = pytrend.build_payload(kw_list=["Quality Education"])
st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

st.header('Gender Equality')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-05_resized.jpg")
q5 = st.slider('How personal is this to you?', 0, 5, key="5")
op5 = pytrend.build_payload(kw_list=["Gender Equality"])
st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

st.header('Clean Water and Sanitation')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-06_resized.jpg")
q6 = st.slider('How personal is this to you?', 0, 5, key="6")
op6 = pytrend.build_payload(kw_list=["Sanitation","Clean Water"])
st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

st.header('Affordable and Clean Energy')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-07_resized.jpg")
q7 = st.slider('How personal is this to you?', 0, 5, key="7")

st.header('Decent Work and Economic Growth')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-08_resized.jpg")
q8 = st.slider('How personal is this to you?', 0, 5, key="8")

st.header('Industry, Innovation and Infrastructure')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-09_resized.jpg")
q9 = st.slider('How personal is this to you?', 0, 5, key="9")

st.header('Reducing Inequality')
st.image("https://www.sustainabilityexchange.ac.uk/images/__e_sdg_goals_icons-individual-cmyk-10_resized.jpg")
q10 = st.slider('How personal is this to you?', 0, 5, key="10")

st.header('Sustainable Cities and Communities')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-11_resized.jpg")
q11 = st.slider('How personal is this to you?', 0, 5, key="11")

st.header('Responsible Consumption and Production')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-12_resized.jpg")
q12 = st.slider('How personal is this to you?', 0, 5, key="12")

st.header('Climate Action')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-13_resized.jpg")
q13 = st.slider('How personal is this to you?', 0, 5, key="13")

st.header('Life Below Water')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-14_resized.jpg")
q14 = st.slider('How personal is this to you?', 0, 5, key="14")

st.header('Life On Land')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-15_resized.jpg")
q15 = st.slider('How personal is this to you?', 0, 5, key="15")

st.header('Peace, Justice, and Strong Institutions')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-16_resized.jpg")
q16 = st.slider('How personal is this to you?', 0, 5, key="16")

st.header('Partnerships for the Goals')
st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-17_resized.jpg")
q17 = st.slider('How personal is this to you?', 0, 5, key="17")








