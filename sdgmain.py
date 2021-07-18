import streamlit as st

import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from streamlit_lottie import st_lottie
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

################
#Author: Jude Rayan
#Class: CPX 4075
################
#References:

#Details and Participating NGO Links for each SDG: https://www.un.org/sustainabledevelopment/
#Stats used for the questionnaire: https://www.afd.fr/en/ressources/quiz-better-understanding-sustainable-development-goals-sdgs
################

##########
#CITATION: “Quiz: Better Understanding the Sustainable Development Goals (SDGs).” AFD - Agence Française de Développement, Agence Française de Développement, Oct. 2017, www.afd.fr/en/ressources/quiz-better-understanding-sustainable-development-goals-sdgs.
##########

pytrend = TrendReq()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets9.lottiefiles.com/datafiles/dc49lw7cOTLEo6y/data.json"
lottie_json = load_lottieurl(lottie_url)

lottie_url2 = "https://assets2.lottiefiles.com/private_files/lf30_lyvbczgo.json"
lottie_json2 = load_lottieurl(lottie_url2)

lottie_url3 = "https://assets9.lottiefiles.com/private_files/lf30_z1sghrbu.json"
lottie_json3 = load_lottieurl(lottie_url3)

data_df = pd.read_csv('https://raw.githubusercontent.com/oterenari/UNSDG/main/Data4.csv')


st.markdown("<h1 style='text-align: center; color: Black;'>UN SDG Recommendation Application</h1>", unsafe_allow_html=True)

#st.header('This tool is a proof of concept to demonstrate the usage of statistical data analysis in applications related to encouraging people to contribute to some of the United Nations Sustainable Development Goals')

st_lottie(lottie_json, key="1")

st.write("A few things to go over, before we start :clipboard:")

st.header("What is the purpose of this application?")
st.write("Hello :wave:, this application is a proof of concept for my class project, to demonstrate the usage of statistical data analysis, in applications related to encouraging people to contribute to the United Nations Sustainable Development Goals. This is a guidance tool.")
#Create Test Array
st.header("How does this tool work?")
st.write("This tool uses a statistical algorithm that processes the responses provided by the user, and tries to match it with people whose problem-solving interests and passions are similarly aligned. The training dataset comprises of the questionnaire responses of the people who have already been able to identify the goals they'd like to contribute to, and those who already have been contributing to a few of them.")
st.header("What data is being used as reference?")
st.write("Since this is a proof of concept, only the responses provided by my fellow classmates (CCPX 4075) to this questionnaire and some synthetic data, is being used as the training dataset. No other form of data is collected. The questionnaire is completely anonymous.")
st_lottie(lottie_json2, key="2")

st.header("Alright, so how do we use this tool?")
st.write('Think about the facts that are presented. Answer the question based on, how aligned these facts/issues are, with your personal passion/ambitions. For example, if you really care about conditions of poverty, but you would play a more indirect role in supporting people who are actively engaged in trying to solve this issue, you would give a rating of 0. On the other hand, if you feel you are inclined to play a more direct role in helping solve these issues, you would rate that response with a 5.')

st.header("Images/Logos and Sustainable Developmental Goal Description Credits:")
st.write("UN Sustainable Goal Development 1 content derived from: https://www.un.org/sustainabledevelopment/poverty/")
st.write("UN Sustainable Goal Development 2 content derived from: https://www.un.org/sustainabledevelopment/hunger/")
st.write("UN Sustainable Goal Development 3 content derived from: https://www.un.org/sustainabledevelopment/health/")
st.write("UN Sustainable Goal Development 4 content derived from: https://www.un.org/sustainabledevelopment/education/")
st.write("UN Sustainable Goal Development 5 content derived from: https://www.un.org/sustainabledevelopment/gender-equality/")
st.write("UN Sustainable Goal Development 6 content derived from: https://www.un.org/sustainabledevelopment/water-and-sanitation/")
st.write("UN Sustainable Goal Development 7 content derived from: https://www.un.org/sustainabledevelopment/energy/")
st.write("UN Sustainable Goal Development 8 content derived from: https://www.un.org/sustainabledevelopment/economic-growth/")
st.write("UN Sustainable Goal Development 9 content derived from: https://www.un.org/sustainabledevelopment/infrastructure-industrialization/")
st.write("UN Sustainable Goal Development 10 content derived from: https://www.un.org/sustainabledevelopment/inequality/")
st.write("UN Sustainable Goal Development 11 content derived from: https://www.un.org/sustainabledevelopment/cities/")
st.write("UN Sustainable Goal Development 12 content derived from: https://www.un.org/sustainabledevelopment/sustainable-consumption-production/")
st.write("UN Sustainable Goal Development 13 content derived from: https://www.un.org/sustainabledevelopment/climate-change/")
st.write("UN Sustainable Goal Development 14 content derived from: https://www.un.org/sustainabledevelopment/oceans/")
st.write("UN Sustainable Goal Development 15 content derived from: https://www.un.org/sustainabledevelopment/biodiversity/")
st.write("UN Sustainable Goal Development 16 content derived from: https://www.un.org/sustainabledevelopment/peace-justice/")
st.write("UN Sustainable Goal Development 13 content derived from: https://www.un.org/sustainabledevelopment/globalpartnerships/")

st.header("Questions for Survey:")
st.text("Derived from: https://www.afd.fr/en/ressources/quiz-better-understanding-sustainable-development-goals-sdgs")



"""

#Maybe add locations where it is popular too
######################################################################################################################################################

#st.markdown("<h1 style='text-align: center; color: green;'>SDG #1: No Poverty</h1>", unsafe_allow_html=True)
with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link: https://www.un.org/sustainabledevelopment/poverty/")


    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?geo=US&q=%2Fg%2F11gbmp432x")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?q=%2Fg%2F11gbmp432x")

    


st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 1 in 7 people live under extreme poverty")
q1 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="1")

st.write("(ii) 1 in 7  people in the world are homeless or live in inadequate housing")
q2 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="2")


st.write("(iii) 82% of the wealth created worldwide in 2017 benefited the richest 1%, but the poorest 50% got nothing.")
q3 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="3")


arr1 = np.array([q1, q2, q3])



with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-01_resized.jpg", width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal1/")
output_check = 0























####################################################################################################################################################################       

#st.markdown("<h1 style='text-align: center; color: green;'>SDG #2: Zero Hunger</h1>", unsafe_allow_html=True)
#q2 = st.slider('How personal is this to you?', 0, 5, key="2")
#op2 = pytrend.build_payload(kw_list=["Hunger"])
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/hunger/")


    st.text("")

    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?geo=US&q=%2Fg%2F11fz0w8dfs")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?q=%2Fg%2F11fz0w8dfs")

  

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 1 in 10 OF THE WORLD’S PEOPLE ARE HUNGRY")
q4 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="4")

st.write("(ii) THE NUMBER OF HUNGRY PEOPLE IN THE WORLD HAS FALLEN SINCE 1990")
q5 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="5")


st.write("(iii) TO FEED THE WORLD IN 2050, FOOD PRODUCTION WILL NEED TO INCREASE BY 70%")
q6 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="6")

arr2 = np.array([q4, q5, q6])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-02_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal2/")

###################################

#st.markdown("<h1 style='text-align: center; color: green;'>SDG #3: Good Health and Well-being</h1>", unsafe_allow_html=True)
##op3 = pytrend.build_payload(kw_list=["Good Health"])
st.write("")
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/health/")
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?geo=US&q=health%20and%20well%20being")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?cat=14&q=health%20and%20well%20being")


st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) The main cause of mortality in the world is an unhealthy environment")
q7 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="7")

st.write("(ii) The main cause of child mortality in developing countries is malnutrition")
q8 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="8")


st.write("(iii) In most countries, climate change will negatively influence air and water quality, the amount of food and safety of housing.")
q9 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="9")

arr3 = np.array([q7, q8, q9])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-03_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal3/")


######################################################################

#st.markdown("<h1 style='text-align: center; color: green;'>SDG #4: Quality Education</h1>", unsafe_allow_html=True)
#op4 = pytrend.build_payload(kw_list=["Quality Education"])
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/education/")
 

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 2 in 10 adults are unable to read and write around the world")
q10 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="10")

st.write("(ii) 66 million children (= population of France) children in developing countries go to school on an empty stomach")
q11 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="11")


st.write("(iii) 1 in 15 children and young people in the world suffer violence or harassment at school")
q12 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="12")

arr4 = np.array([q10, q11, q12])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-04_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal4/")

###########################################################################################
#st.markdown("<h1 style='text-align: center; color: green;'>SDG #5: Gender Equality</h1>", unsafe_allow_html=True)
##op5 = pytrend.build_payload(kw_list=["Gender Equality"])
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))
with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/gender-equality/")
    

    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?geo=US&q=gender%20equality")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?q=gender%20equality")
 

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) According to the world economic forum, gender inequalities at work will not disappear until 2234")
q13 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="13")

st.write("(ii) The percentage of researchers who are women, are only 29%")
q14 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="14")

st.write("(iii) Two-thirds of the 815 million people unable to read or write in the world, are women")
q15 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="15")

arr5 = np.array([q13, q14, q15])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-05_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal5/")

st.text("")

############################################################################

#st.markdown("<h1 style='text-align: center; color: green;'>SDG #6: Clean Water and Sanitation</h1>", unsafe_allow_html=True)
#st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-06_resized.jpg")
#op6 = pytrend.build_payload(kw_list=["Sanitation","Clean Water"])

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/water-and-sanitation/")
    
    


st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Less than 3% of the world’s water is fresh")
q16 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="16")

st.write("(ii) 1 in 3 people do not have access to clean and sanitary toilets.")
q17 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="17")

st.write("(iii) 90% of wastewater from human activity is discharged back into the rivers and seas without being treated")
q18 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="18")

arr6 = np.array([q16, q17, q18])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-06_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal6/")


################################################################################################################

#st.markdown("<h1 style='text-align: center; color: green;'>SDG #7: Affordable and Clean Energy</h1>", unsafe_allow_html=True)

st.write("")
#op6 = pytrend.build_payload(kw_list=["Clean Energy","Affordablce"])

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/energy/")
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?geo=US&q=Affordable%20and%20Clean%20Energy")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?q=Affordable%20and%20Clean%20Energy")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Humankind generates between 80 to 130 tonnes of waste per second")
q19 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="19")

st.write("(ii) 1.3 billion people(or the population of China) do not have access to electricity in the world")
q20 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="20")

st.write("(iii) 200 million people (or 3% of the world’s population) are unemployed")
q21 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="21")

arr7 = np.array([q19, q20, q21])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-07_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal7/")


##############################################
#st.markdown("<h1 style='text-align: center; color: green;'>SDG #8: Decent Work and Economic Growth</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Decent Work","Economic Growth"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/economic-growth/")
    
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?geo=US&q=Economic%20Growth")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?q=Economic%20Growth")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) One worker dies from a work-related accident or disease every 15 seconds - occupational disease")
q22 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="22")

st.write("(ii) Global rate of employment for disabled people is lower than that of able-bodied people")
q23 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="23")

st.write("(iii) 30 million jobs need to be created each year to keep up with the growth in the world’s active population")
q24 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="24")

arr8 = np.array([q22, q23, q24])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-08_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal8/")


####################################################################################################
#st.markdown("<h1 style='text-align: center; color: green;'>SDG #9: Industry, Innovation and Infrastructure</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Industry","Innovation"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/infrastructure-industrialization/")
    
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?geo=US&q=Industry,innovation,infrastructure")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?q=Industry,innovation,infrastructure")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 95% of the population in developing countries has no internet access")
q25 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="25")

st.write("(ii) Between 1 and 1.5 billion people today, have no access to reliable telecommunications services")
q26 = st.slider('Rate this on a scale from 0 to 5', 0, 5, key="26")

st.write("(iii) In low-income countries, infrastructure constraints affect company productivity by nearly 40%")
q27 = st.slider('Rate this on a scale from 0 to 5', 0, 5, key="27")

arr9 = np.array([q25, q26, q27])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-09_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal9/")

#######################################################################

#st.markdown("<h1 style='text-align: center; color: green;'>SDG #10: Reducing Inequalities</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Inequality"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/inequality/")
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?cat=14&geo=US&q=Inequalities")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?cat=14&q=Inequalities")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 75% of the population live in societies where incomes are more unequally distributed than in the 1990s")
q28 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="28")

st.write("(ii) Women in urban areas are three times less likely to die during childbirth than those living in rural areas")
q29 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="29")

st.write("(iii) 83% of domestic workers around the world are women")
q30 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="30")

arr10 = np.array([q28, q29, q30])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-10_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal10/")

##################################################################################
#st.markdown("<h1 style='text-align: center; color: green;'>SDG #11: Sustainable Cities and Communities</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Sustainable Cities"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/cities/")
    
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?cat=14&geo=US&q=sustainable%20cities")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?cat=14&q=sustainable%20cities")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) By 2030, if nothing is done 3 billion, or 1 in 5 people will be living in shanty towns")
q31 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="31")

st.write("(ii) Rapid urbanization puts pressure on economic growth")
q32 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="32")

st.write("(iii) 1 in 8 people live in shanty towns around the world")
q33 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="33")

arr11 = np.array([q31, q32, q33])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-11_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal11/")



########
#st.markdown("<h1 style='text-align: center; color: green;'>SDG #12: Responsible Consumption and Production</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Responsible Consumption"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/sustainable-consumption-production/")
    
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?cat=14&geo=US&q=consumption%20and%20production")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?cat=14&q=consumption%20and%20production")

    

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) One-third of all food produced is wasted or thrown away")
q34 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="34")

st.write("(ii) 250 km3 of water are used unnecessarily each year in the production of wasted food")
q35 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="35")

st.write("(iii) If the entire world population were to use energy-efficient light bulbs, we would save 120 billion dollars a year")
q36 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="36")

arr12 = np.array([q34, q35, q36])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-12_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal12/")

###################################
#st.markdown("<h1 style='text-align: center; color: green;'>SDG #13: Climate Action</h1>", unsafe_allow_html=True)

st.write("")
#sop8 = pytrend.build_payload(kw_list=["Climate"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/climate-change/")
    
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?cat=14&geo=US&q=climate%20action")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?cat=14&q=climate%20action")

  

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Without greenhouse gases, the temperature would be -19c")
q37 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="37")

st.write("(ii) Since 1979, sea ice has diminished by 1 million km2 each decade (or 100,000 football pitches)")
q38 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="38")

st.write("(iii) Since 1990, global carbon dioxide (co2)emissions have increased by almost 50%")
q39 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="39")

arr13 = np.array([q37, q38, q39])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-13_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal13/")

################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #14: Life Below Water</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Life Below Water"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/oceans/")
    

  

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i)  At the current rate, there will be more plastic in the oceans than fish by 2050")
q40 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="40")

st.write("(ii) More than 3 billion people depend on marine biodiversity for their livelihoods")
q41 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="41")

st.write("(iii) 80% of commercial fisheries are over or fully exploited")
q42 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="42")

arr14 = np.array([q40, q41, q42])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-14_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal14/")

#######################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #15: Life on Land</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Life Below Water"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/biodiversity/")
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?cat=14&geo=US&q=life%20on%20land")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?cat=14&q=life%20on%20land")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 13 million hectares (15 million football pitches) hectares of forest are disappearing every year")
q43 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="43")

st.write("(ii) 1 in 5 people rely on forests for their livelihood around the world")
q44 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="44")

st.write("(iii) Of all known animal species… 8% are already extinct and 22% are facing extinction")
q45 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="45")

with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-15_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal15/")

arr15 = np.array([q43, q44, q45])


########################################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #16: Peace, Justice and Strong</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Life Below Water"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/peace-justice/")
    
    
    st.header("Explore the related trending topics")
    st.subheader("In the United States:")
    st.write("https://trends.google.com/trends/explore?cat=14&geo=US&q=peace%20and%20justice")
    st.subheader("Worldwide:")
    st.write("https://trends.google.com/trends/explore?cat=14&q=peace%20and%20justice")




st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Justice and the police institutions are most affected by corruption in the world")
q46 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="46")

st.write("(ii) 1 in 9, or 230 million children live in regions threatened by conflict")
q47 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="47")

st.write("(iii) 1 in 2 children aged 6 to 17 live in a country where corporal punishment is not completely banned in school")
q48 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="48")

arr16 = np.array([q46, q47, q48])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-16_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal16/")

######

st.markdown("<h1 style='text-align: center; color: green;'>SDG #17: Partnerships for the Goals</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Life Below Water"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Link Description: https://www.un.org/sustainabledevelopment/globalpartnerships/")
    
    





st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Development assistance is financial assistance from the richest to the poorest countries")
q49 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="49")

st.write("(ii) Since 2009, the number of web users in the developing countries has more than doubled")
q50 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="50")

st.write("(iii) EUR 800 billion is diverted each year from the developing countries to the countries of the north")
q51 = st.slider('Rate this on a scale from 0 to 4', 0, 4, key="51")

arr17 = np.array([q49, q50, q51])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-17_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal17/")




test_array = np.array([arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,arr9,arr10,arr11,arr12,arr13,arr14,arr15,arr16,arr17])
result = test_array.flatten()




data_df.drop(data_df.columns[0],axis=1,inplace=True)

#st.write("")
#st.write("After splitting")
#st.write("")
split_at = 17
left = data_df.iloc[:, :split_at]
#st.write(left)
right = data_df.iloc[:, split_at:]
#st.write(right)

#st.write(data_df)


#X_train = [[1.0, 2.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]]
st.write('')
st.markdown("<h1 style='text-align: center; color: black;'>You've completed the questionnaire</h1>", unsafe_allow_html=True)
st_lottie(lottie_json3, key="3")
st.write("")
st.header("Now click on Analyze to calculate recommendations.")
analyze_button = st.button("Analyze")

sdg1=0
sdg2=0
sdg3=0

if analyze_button:
    with st.spinner('Wait for it...'):         
        X_train = right.to_numpy()


        X_train_arr = np.array(X_train)
        #st.write(X_train_arr)
        #y_train = [['Hello'], ['this'], ['is'], ['test']]
        #y_train = [[0,1,1], [1,0,0], [0,0,0], [1,0,1]]
        y_train = left.to_numpy()
        neigh = KNeighborsClassifier(n_neighbors=3, n_jobs=8)
        neigh.fit(X_train, y_train)
        X_test = [result]

        prediction = neigh.predict(X_test)
        distances, indices = neigh.kneighbors(X_test)

        #st.write([y_train[i] for i in indices[0]])
        st.title("Your top 3 recommendation sets are:")
        #st.write(indices[0])
        
        user1 = indices[0][0]
        
        user2 = indices[0][1]
        
        user3 = indices[0][2]
       
        user1_data = left.loc[user1,:]
        #st.write(user1_data)
        #st.write(user1_data.shape)
        user2_data = left.loc[user2,:]
        #st.write(user2_data)
        user3_data = left.loc[user3,:]
        #st.write(user3_data)
        
        fo1 = np.where(user1_data)[0]
        
        fo2 = np.where(user2_data)[0]
        
        fo3 = np.where(user3_data)[0]
 
        st.write("Set 1")
        st.write(fo1)
        st.write("")
        st.write("Set 2")
        st.write(fo2)
        st.write("")
        st.write("Set 3")
        st.write(fo3)

        st.subheader('Key:')
        st.write("0: No Poverty")
        st.write("1: Zero Hunger")
        st.write("2: Good Health and Well-being")
        st.write("3: Quality Education")
        st.write("4: Gender Equality")
        st.write("5: Clean Water and Sanitation")
        st.write("6: Affordable and Clean Energy")
        st.write("7: Decent Work and Economic Growth")
        st.write("8: Industry, Innovation and Infrastructure")
        st.write("9: Reducing Inequalities")
        st.write("10: Sustainable Cities and Communities")
        st.write("11: Responsible Consumption and Production")
        st.write("12: Climate Action")
        st.write("13: Life Below Water")
        st.write("14: Life on Land")
        st.write("15: Peace, Justice and Strong")
        st.write("16: Partnerships for the Goals")

        














 """
