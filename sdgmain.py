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
#References:

#Details and Participating NGO Links for each SDG: https://www.un.org/sustainabledevelopment/
#Stats used for the questionnaire: https://www.afd.fr/en/ressources/quiz-better-understanding-sustainable-development-goals-sdgs
################


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

data_df = pd.read_csv("/Users/macbookpro/Downloads/Data3.csv")



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


#Maybe add locations where it is popular too
######################################################################################################################################################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #1: No Poverty</h1>", unsafe_allow_html=True)
with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Globally, the number of people living in extreme poverty declined from 36 per cent in 1990 to 10 per cent in 2015. But the pace of change is decelerating and the COVID-19 crisis risks reversing decades of progress in the fight against poverty. New research published by the UNU World Institute for Development Economics Research warns that the economic fallout from the global pandemic could increase global poverty by as much as half a billion people, or 8% of the total human population. This would be the first time that poverty has increased globally in thirty years, since 1990.") 
    st.text("")
    st.write("More than 700 million people, or 10 per cent of the world population, still live in extreme poverty today, struggling to fulfil the most basic needs like health, education, and access to water and sanitation, to name a few. The majority of people living on less than $1.90 a day live in sub-Saharan Africa. Worldwide, the poverty rate in rural areas is 17.2 per cent—more than three times higher than in urban areas.")  
    st.text("")
    st.write(
    "For those who work, having a job does not guarantee a decent living. In fact, 8 per cent of employed workers and their families worldwide lived in extreme poverty in 2018. One out of five children live in extreme poverty. Ensuring social protection for all children and other vulnerable groups is critical to reduce poverty.")

    st.text("")


st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 1 in 7 people live under extreme poverty")
q1 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="1")

st.write("(ii) 1 in 7  people in the world are homeless or live in inadequate housing")
q2 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="2")


st.write("(iii) 82% of the wealth created worldwide in 2017 benefited the richest 1%, but the poorest 50% got nothing.")
q3 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="3")


arr1 = np.array([q1, q2, q3])



with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-01_resized.jpg", width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal1/")
output_check = 0























####################################################################################################################################################################       

st.markdown("<h1 style='text-align: center; color: green;'>SDG #2: Zero Hunger</h1>", unsafe_allow_html=True)
#q2 = st.slider('How personal is this to you?', 0, 5, key="2")
#op2 = pytrend.build_payload(kw_list=["Hunger"])
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("After decades of steady decline, the number of people who suffer from hunger – as measured by the prevalence of undernourishment – began to slowly increase again in 2015. Current estimates show that nearly 690 million people are hungry, or 8.9 percent of the world population – up by 10 million people in one year and by nearly 60 million in five years.") 
    st.text("")
    st.write("The world is not on track to achieve Zero Hunger by 2030. If recent trends continue, the number of people affected by hunger would surpass 840 million by 2030.")  
    st.text("")
    st.write("According to the World Food Programme, 135 million suffer from acute hunger largely due to man-made conflicts, climate change and economic downturns. The COVID-19 pandemic could now double that number, putting an additional 130 million people at risk of suffering acute hunger by the end of 2020.")
    st.text("")
    st.write("With more than a quarter of a billion people potentially at the brink of starvation, swift action needs to be taken to provide food and humanitarian relief to the most at-risk regions.")
    st.text("")
    st.write("At the same time, a profound change of the global food and agriculture system is needed if we are to nourish the more than 690 million people who are hungry today – and the additional 2 billion people the world will have by 2050. Increasing agricultural productivity and sustainable food production are crucial to help alleviate the perils of hunger.")

    st.text("")
  

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 1 in 10 OF THE WORLD’S PEOPLE ARE HUNGRY")
q4 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="4")

st.write("(ii) THE NUMBER OF HUNGRY PEOPLE IN THE WORLD HAS FALLEN SINCE 1990")
q5 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="5")


st.write("(iii) TO FEED THE WORLD IN 2050, FOOD PRODUCTION WILL NEED TO INCREASE BY 70%")
q6 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="6")

arr2 = np.array([q4, q5, q6])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-02_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal2/")

###################################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #3: Good Health and Well-being</h1>", unsafe_allow_html=True)
##op3 = pytrend.build_payload(kw_list=["Good Health"])
st.write("")
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Ensuring healthy lives and promoting well-being at all ages is essential to sustainable development. Currently, the world is facing a global health crisis unlike any other — COVID-19 is spreading human suffering, destabilizing the global economy and upending the lives of billions of people around the globe")
    st.text("")
    st.write("Before the pandemic, major progress was made in improving the health of millions of people. Significant strides were made in increasing life expectancy and reducing some of the common killers associated with child and maternal mortality. But more efforts are needed to fully eradicate a wide range of diseases and address many different persistent and emerging health issues. By focusing on providing more efficient funding of health systems, improved sanitation and hygiene, and increased access to physicians, significant progress can be made in helping to save the lives of millions.")
    st.text("")
    st.write("Health emergencies such as COVID-19 pose a global risk and have shown the critical need for preparedness. The United Nations Development Programme highlighted huge disparities in countries’ abilities to cope with and recover from the COVID-19 crisis. The pandemic provides a watershed moment for health emergency preparedness and for investment in critical 21st century public services. ")
    st.text("")


st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) The main cause of mortality in the world is an unhealthy environment")
q7 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="7")

st.write("(ii) The main cause of child mortality in developing countries is malnutrition")
q8 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="8")


st.write("(iii) In most countries, climate change will negatively influence air and water quality, the amount of food and safety of housing.")
q9 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="9")

arr3 = np.array([q7, q8, q9])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-03_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal3/")


######################################################################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #4: Quality Education</h1>", unsafe_allow_html=True)
#op4 = pytrend.build_payload(kw_list=["Quality Education"])
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Education enables upward socioeconomic mobility and is a key to escaping poverty. Over the past decade, major progress was made towards increasing access to education and school enrollment rates at all levels, particularly for girls. Nevertheless, about 260 million children were still out of school in 2018 — nearly one fifth of the global population in that age group. And more than half of all children and adolescents worldwide are not meeting minimum proficiency standards in reading and mathematics. ")
    st.text("")
    st.write("In 2020, as the COVID-19 pandemic spread across the globe, a majority of countries announced the temporary closure of schools, impacting more than 91 per cent of students worldwide. By April 2020, close to 1.6 billion children and youth were out of school. And nearly 369 million children who rely on school meals needed to look to other sources for daily nutrition. ")
    st.text("")
    st.write("Never before have so many children been out of school at the same time, disrupting learning and upending lives, especially the most vulnerable and marginalised. The global pandemic has far-reaching consequences that may jeopardize hard won gains made in improving global education.")
    st.text("")
 

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 2 in 10 adults are unable to read and write around the world")
q10 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="10")

st.write("(ii) 66 million children (= population of France) children in developing countries go to school on an empty stomach")
q11 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="11")


st.write("(iii) 1 in 15 children and young people in the world suffer violence or harassment at school")
q12 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="12")

arr4 = np.array([q10, q11, q12])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-04_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal4/")

###########################################################################################
st.markdown("<h1 style='text-align: center; color: green;'>SDG #5: Gender Equality</h1>", unsafe_allow_html=True)
##op5 = pytrend.build_payload(kw_list=["Gender Equality"])
#st.write(pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))
with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Gender equality is not only a fundamental human right, but a necessary foundation for a peaceful, prosperous and sustainable world. ")
    st.text("")
    st.write("There has been progress over the last decades: More girls are going to school, fewer girls are forced into early marriage, more women are serving in parliament and positions of leadership, and laws are being reformed to advance gender equality. ")
    st.text("")
    st.write("Despite these gains, many challenges remain: discriminatory laws and social norms remain pervasive, women continue to be underrepresented at all levels of political leadership, and 1 in 5 women and girls between the ages of 15 and 49 report experiencing physical or sexual violence by an intimate partner within a 12-month period.")
    st.text("")
    st.write("The effects of the COVID-19 pandemic could reverse the limited progress that has been made on gender equality and women’s rights.  The coronavirus outbreak exacerbates existing inequalities for women and girls across every sphere – from health and the economy, to security and social protection. ")
    st.text("")
    st.write("Women play a disproportionate role in responding to the virus, including as frontline healthcare workers and carers at home. Women’s unpaid care work has increased significantly as a result of school closures and the increased needs of older people. Women are also harder hit by the economic impacts of COVID-19, as they disproportionately work in insecure labour markets. Nearly 60 per cent of women work in the informal economy, which puts them at greater risk of falling into poverty.")
    st.text("")
    st.write("The pandemic has also led to a steep increase in violence against women and girls. With lockdown measures in place, many women are trapped at home with their abusers, struggling to access services that are suffering from cuts and restrictions. Emerging data shows that, since the outbreak of the pandemic, violence against women and girls – and particularly domestic violence – has intensified.")
    st.text("")
 

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) According to the world economic forum, gender inequalities at work will not disappear until 2234")
q13 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="13")

st.write("(ii) The percentage of researchers who are women, are only 29%")
q14 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="14")

st.write("(iii) Two-thirds of the 815 million people unable to read or write in the world, are women")
q15 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="15")

arr5 = np.array([q13, q14, q15])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-05_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal5/")

st.text("")

############################################################################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #6: Clean Water and Sanitation</h1>", unsafe_allow_html=True)
#st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-06_resized.jpg")
#op6 = pytrend.build_payload(kw_list=["Sanitation","Clean Water"])

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("While substantial progress has been made in increasing access to clean drinking water and sanitation, billions of people—mostly in rural areas—still lack these basic services. Worldwide, one in three people do not have access to safe drinking water, two out of five people do not have a basic hand-washing facility with soap and water, and more than 673 million people still practice open defecation.")
    st.text("")
    st.write("The COVID-19 pandemic has demonstrated the critical importance of sanitation, hygiene and adequate access to clean water for preventing and containing diseases. Hand hygiene saves lives. According to the World Health Organization, handwashing is one of the most effective actions you can take to reduce the spread of pathogens and prevent infections, including the COVID-19 virus. Yet billions of people still lack safe water sanitation, and funding is inadequate.")
    st.text("")
    


st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Less than 3% of the world’s water is fresh")
q16 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="16")

st.write("(ii) 1 in 3 people do not have access to clean and sanitary toilets.")
q17 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="17")

st.write("(iii) 90% of wastewater from human activity is discharged back into the rivers and seas without being treated")
q18 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="18")

arr6 = np.array([q16, q17, q18])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-06_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal6/")


################################################################################################################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #7: Affordable and Clean Energy</h1>", unsafe_allow_html=True)

st.write("")
#op6 = pytrend.build_payload(kw_list=["Clean Energy","Affordablce"])

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("The world is making progress towards Goal 7, with encouraging signs that energy is becoming more sustainable and widely available. Access to electricity in poorer countries has begun to accelerate, energy efficiency continues to improve, and renewable energy is making impressive gains in the electricity sector. ")
    st.text("")
    st.write("Nevertheless, more focused attention is needed to improve access to clean and safe cooking fuels and technologies for 3 billion people, to expand the use of renewable energy beyond the electricity sector, and to increase electrification in sub-Saharan Africa.")
    st.text("")
    st.write("The Energy Progress Report provides global dashboard to register progress on energy access, energy efficiency and renewable energy. It assesses the progress made by each country on these three pillars and provides a snapshot of how far we are from achieving the 2030 Sustainable Development Goals targets.")
    st.text("")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Humankind generates between 80 to 130 tonnes of waste per second")
q19 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="19")

st.write("(ii) 1.3 billion people(or the population of China) do not have access to electricity in the world")
q20 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="20")

st.write("(iii) 200 million people (or 3% of the world’s population) are unemployed")
q21 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="21")

arr7 = np.array([q19, q20, q21])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-07_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal7/")


##############################################
st.markdown("<h1 style='text-align: center; color: green;'>SDG #8: Decent Work and Economic Growth</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Decent Work","Economic Growth"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Sustained and inclusive economic growth can drive progress, create decent jobs for all and improve living standards. ")
    st.text("")
    st.write("COVID-19 has disrupted billions of lives and endangered the global economy. The International Monetary Fund (IMF) expects a global recession as bad as or worse than in 2009. As job losses escalate, the International Labor Organization estimates that nearly half of the global workforce is at risk of losing their livelihoods.")
    st.text("")
    st.write("Even before the outbreak of COVID-19, one in five countries – home to billions of people living in poverty – were likely to see per capita incomes stagnate or decline in 2020. Now, the economic and financial shocks associated with COVID-19—such as disruptions to industrial production, falling commodity prices, financial market volatility, and rising insecurity—are derailing the already tepid economic growth and compounding heightened risks from other factors.")
    st.text("")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) One worker dies from a work-related accident or disease every 15 seconds - occupational disease")
q22 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="22")

st.write("(ii) Global rate of employment for disabled people is lower than that of able-bodied people")
q23 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="23")

st.write("(iii) 30 million jobs need to be created each year to keep up with the growth in the world’s active population")
q24 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="24")

arr8 = np.array([q22, q23, q24])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-08_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal8/")


####################################################################################################
st.markdown("<h1 style='text-align: center; color: green;'>SDG #9: Industry, Innovation and Infrastructure</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Industry","Innovation"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Inclusive and sustainable industrialization, together with innovation and infrastructure, can unleash dynamic and competitive economic forces that generate employment and income. They play a key role in introducing and promoting new technologies, facilitating international trade and enabling the efficient use of resources. ")
    st.text("")
    st.write("However, the world still has a long way to go to fully tap this potential. Least developed countries, in particular, need to accelerate the development of their manufacturing sector if they are to meet the 2030 target, and scale up investment in scientific research and innovation. ")
    st.text("")
    st.write("Global manufacturing growth has been steadily declining, even before the outbreak of the COVID-19 pandemic. The pandemic is hitting manufacturing industries hard and causing disruptions in global value chains and the supply of products. ")
    st.text("")
    st.write("Innovation and technological progress are key to finding lasting solutions to both economic and environmental challenges, such as increased resource and energy-efficiency. Globally, investment in research and development (R&D) as a proportion of GDP increased from 1.5 per cent in 2000 to 1.7 per cent in 2015 and remained almost unchanged in 2017, but was only less than 1 per cent  in developing regions.")
    st.text("")
    st.write("In terms of communications infrastructure, more than half of the world’s population is now online and almost the entire world population lives in an area covered by a mobile network. It is estimated that in 2019, 96.5 per cent were covered by at least a 2G network.")
    st.text("")
    st.write("The coronavirus pandemic has revealed the urgent need for resilient infrastructure. The Asian Development Bank notes that critical infrastructure in the region remains far from adequate in many countries, despite the rapid economic growth and development the region has experienced over the past decade. The Economic and Social Survey of Asia and the Pacific highlights that making infrastructure resilient to disasters and climate change will require an additional investment of $434 billion per year. This sum may need to be even greater in some subregions, such as the Pacific small island developing states.")
    st.text("")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 95% of the population in developing countries has no internet access")
q25 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="25")

st.write("(ii) Between 1 and 1.5 billion people today, have no access to reliable telecommunications services")
q26 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="26")

st.write("(iii) In low-income countries, infrastructure constraints affect company productivity by nearly 40%")
q27 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="27")

arr9 = np.array([q25, q26, q27])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-09_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal9/")

#######################################################################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #10: Reducing Inequalities</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Inequality"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Reducing inequalities and ensuring no one is left behind are integral to achieving the Sustainable Development Goals.")
    st.text("")
    st.write("Inequality within and among countries is a persistent cause for concern. Despite some positive signs toward reducing inequality in some dimensions, such as reducing relative income inequality in some countries and preferential trade status benefiting lower-income countries, inequality still persists.")
    st.text("")
    st.write("COVID-19 has deepened existing inequalities, hitting the poorest and most vulnerable communities the hardest. It has put a spotlight on economic inequalities and fragile social safety nets that leave vulnerable communities to bear the brunt of the crisis.  At the same time, social, political and economic inequalities have amplified the impacts of the pandemic.")
    st.text("")
    st.write("On the economic front, the COVID-19 pandemic has significantly increased global unemployment and dramatically slashed workers’ incomes.")
    st.text("")
    st.write("COVID-19 also puts at risk the limited progress that has been made on gender equality and women’s rights over the past decades. Across every sphere, from health to the economy, security to social protection, the impacts of COVID-19 are exacerbated for women and girls simply by virtue of their sex.")
    st.text("")
    st.write("Inequalities are also deepening for vulnerable populations in countries with weaker health systems and those facing existing humanitarian crises. Refugees and migrants, as well as indigenous peoples, older persons, people with disabilities and children are particularly at risk of being left behind. And hate speech targeting vulnerable groups is rising.")
    st.text("")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 75% of the population live in societies where incomes are more unequally distributed than in the 1990s")
q28 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="28")

st.write("(ii) Women in urban areas are three times less likely to die during childbirth than those living in rural areas")
q29 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="29")

st.write("(iii) 83% of domestic workers around the world are women")
q30 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="30")

arr10 = np.array([q28, q29, q30])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-10_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal10/")

##################################################################################
st.markdown("<h1 style='text-align: center; color: green;'>SDG #11: Sustainable Cities and Communities</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Sustainable Cities"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("The world is becoming increasingly urbanized. Since 2007, more than half the world’s population has been living in cities, and that share is projected to rise to 60 per cent by 2030.")
    st.text("")
    st.write("Cities and metropolitan areas are powerhouses of economic growth—contributing about 60 per cent of global GDP. However, they also account for about 70 per cent of global carbon emissions and over 60 per cent of resource use. ")
    st.text("")
    st.write("Rapid urbanization is resulting in a growing number of slum dwellers, inadequate and overburdened infrastructure and services (such as waste collection and water and sanitation systems, roads and transport), worsening air pollution and unplanned urban sprawl. ")
    st.text("")
    st.write("The impact of COVID-19 will be most devastating in poor and densely populated urban areas, especially for the one billion people living in informal settlements and slums worldwide, where overcrowding also makes it difficult to follow recommended measures such as social distancing and self-isolation. ")
    st.text("")
    st.write("The UN food agency, FAO, warned that hunger and fatalities could rise significantly in urban areas, without measures to ensure that poor and vulnerable residents have access to food.")
    st.text("")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) By 2030, if nothing is done 3 billion, or 1 in 5 people will be living in shanty towns")
q31 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="31")

st.write("(ii) Rapid urbanization puts pressure on economic growth")
q32 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="32")

st.write("(iii) 1 in 8 people live in shanty towns around the world")
q33 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="33")

arr11 = np.array([q31, q32, q33])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-11_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal11/")



########
st.markdown("<h1 style='text-align: center; color: green;'>SDG #12: Responsible Consumption and Production</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Responsible Consumption"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Worldwide consumption and production — a driving force of the global economy — rest on the use of the natural environment and resources in a way that continues to have destructive impacts on the planet. ")
    st.text("")
    st.write("Economic and social progress over the last century has been accompanied by environmental degradation that is endangering the very systems on which our future development — indeed, our very survival — depends. ")
    st.text("")
    st.write("A few facts and figures:Each year, an estimated one third of all food produced – equivalent to 1.3 billion tonnes worth around $1 trillion – ends up rotting in the bins of consumers and retailers, or spoiling due to poor transportation and harvesting practices. If people worldwide switched to energy efficient light bulbs the world would save US$120 billion annually. Should the global population reach 9.6 billion by 2050, the equivalent of almost three planets could be required to provide the natural resources needed to sustain current lifestyles.")
    st.text("")
    st.write("The COVID-19 pandemic offers countries an opportunity to build recovery plans that will reverse current trends and change our consumption and production patterns towards a more sustainable future.")
    st.text("")
    st.write("Sustainable consumption and production is about doing more and better with less. It is also about decoupling economic growth from environmental degradation, increasing resource efficiency and promoting sustainable lifestyles.")
    st.text("")
    st.write("Sustainable consumption and production can also contribute substantially to poverty alleviation and the transition towards low-carbon and green economies.")
    st.text("")

    

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) One-third of all food produced is wasted or thrown away")
q34 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="34")

st.write("(ii) 250 km3 of water are used unnecessarily each year in the production of wasted food")
q35 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="35")

st.write("(iii) If the entire world population were to use energy-efficient light bulbs, we would save 120 billion dollars a year")
q36 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="36")

arr12 = np.array([q34, q35, q36])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-12_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal12/")

###################################
st.markdown("<h1 style='text-align: center; color: green;'>SDG #13: Climate Action</h1>", unsafe_allow_html=True)

st.write("")
#sop8 = pytrend.build_payload(kw_list=["Climate"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("2019 was the second warmest year on record and the end of the warmest decade (2010- 2019) ever recorded. ")
    st.text("")
    st.write("Carbon dioxide (CO2) levels and other greenhouse gases in the atmosphere rose to new records in 2019. ")
    st.text("")
    st.write("Climate change is affecting every country on every continent. It is disrupting national economies and affecting lives. Weather patterns are changing, sea levels are rising, and weather events are becoming more extreme.")
    st.text("")
    st.write("Although greenhouse gas emissions are projected to drop about 6 per cent in 2020 due to travel bans and economic slowdowns resulting from the COVID-19 pandemic, this improvement is only temporary. Climate change is not on pause. Once the global economy begins to recover from the pandemic, emissions are expected to return to higher levels.")
    st.text("")
    st.write("Saving lives and livelihoods requires urgent action to address both the pandemic and the climate emergency")
    st.text("")
    st.write("The Paris Agreement, adopted in 2015, aims to strengthen the global response to the threat of climate change by keeping a global temperature rise this century well below 2 degrees Celsius above pre-industrial levels. The agreement also aims to strengthen the ability of countries to deal with the impacts of climate change, through appropriate financial flows, a new technology framework and an enhanced capacity building framework.")
    st.text("")

  

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Without greenhouse gases, the temperature would be -19c")
q37 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="37")

st.write("(ii) Since 1979, sea ice has diminished by 1 million km2 each decade (or 100,000 football pitches)")
q38 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="38")

st.write("(iii) Since 1990, global carbon dioxide (co2)emissions have increased by almost 50%")
q39 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="39")

arr13 = np.array([q37, q38, q39])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-13_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal13/")

################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #14: Life Below Water</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Life Below Water"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("2The ocean drives global systems that make the Earth habitable for humankind. Our rainwater, drinking water, weather, climate, coastlines, much of our food, and even the oxygen in the air we breathe, are all ultimately provided and regulated by the sea. ")
    st.text("")
    st.write("Careful management of this essential global resource is a key feature of a sustainable future. However, at the current time, there is a continuous deterioration of coastal waters owing to pollution, and ocean acidification is having an adversarial effect on the functioning of ecosystems and biodiversity. This is also negatively impacting small scale fisheries. ")
    st.text("")
    st.write("Saving our ocean must remain a priority. Marine biodiversity is critical to the health of people and our planet. Marine protected areas need to be effectively managed and well-resourced and regulations need to be put in place to reduce overfishing, marine pollution and ocean acidification.")
    st.text("")

  

st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i)  At the current rate, there will be more plastic in the oceans than fish by 2050")
q40 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="40")

st.write("(ii) More than 3 billion people depend on marine biodiversity for their livelihoods")
q41 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="41")

st.write("(iii) 80% of commercial fisheries are over or fully exploited")
q42 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="42")

arr14 = np.array([q40, q41, q42])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-14_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal14/")

#######################

st.markdown("<h1 style='text-align: center; color: green;'>SDG #15: Life on Land</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Life Below Water"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("Nature is critical to our survival: nature provides us with our oxygen, regulates our weather patterns, pollinates our crops, produces our food, feed and fibre. But it is under increasing stress. Human activity has altered almost 75 per cent of the earth’s surface, squeezing wildlife and nature into an ever-smaller corner of the planet.")
    st.text("")
    st.write("Around 1 million animal and plant species are threatened with extinction – many within decades – according to the 2019 Global Assessment Report on Biodiversity and Ecosystem Service. The report called for transformative changes to restore and protect nature. It found that the health of ecosystems on which we and all other species depend is deteriorating more rapidly than ever, affecting  the very foundations of our economies, livelihoods, food security, health and quality of life worldwide. ")
    st.text("")
    st.write("Deforestation and desertification – caused by human activities and climate change – pose major challenges to sustainable development and have affected the lives and livelihoods of millions of people. Forests are vitally important for sustaining life on Earth, and play a major role in the fight against climate change. And investing in land restoration is critical for improving livelihoods, reducing vulnerabilities, and reducing risks for the economy.")
    st.text("")
    st.write("The health of our planet also plays an important role in the emergence of zoonotic diseases, i.e. diseases that are transmissible between animals and humans. As we continue to encroach on fragile ecosystems, we bring humans into ever-greater contact with wildlife, enabling pathogens in wildlife to spill over to livestock and humans, increasing the risk of disease emergence and amplification.")
    st.text("")



st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) 13 million hectares (15 million football pitches) hectares of forest are disappearing every year")
q43 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="43")

st.write("(ii) 1 in 5 people rely on forests for their livelihood around the world")
q44 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="44")

st.write("(iii) Of all known animal species… 8% are already extinct and 22% are facing extinction")
q45 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="45")

with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
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
    st.write("Conflict, insecurity, weak institutions and limited access to justice remain a great threat to sustainable development.")
    st.text("")
    st.write("The number of people fleeing war, persecution and conflict exceeded 70 million in 2018, the highest level recorded by the UN refugee agency (UNHCR) in almost 70 years")
    st.text("")
    st.write("In 2019, the United Nations tracked 357 killings and 30 enforced disappearances of human rights defenders, journalists and trade unionists in 47 countries.")
    st.text("")
    st.write("And the births of around one in four children under age 5 worldwide are never officially recorded, depriving them of a proof of legal identity crucial for the protection of their rights and for access to justice and social services.")
    st.text("")




st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Justice and the police institutions are most affected by corruption in the world")
q46 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="46")

st.write("(ii) 1 in 9, or 230 million children live in regions threatened by conflict")
q47 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="47")

st.write("(iii) 1 in 2 children aged 6 to 17 live in a country where corporal punishment is not completely banned in school")
q48 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="48")

arr16 = np.array([q46, q47, q48])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
            st.image("https://www.sustainabilityexchange.ac.uk/images/e_sdg_goals_icons-individual-cmyk-16_resized.jpg",width=200)
            st.write("https://sustainabledevelopment.un.org/partnerships/goal16/")

######

st.markdown("<h1 style='text-align: center; color: green;'>SDG #17: Partnerships for the Goals</h1>", unsafe_allow_html=True)

st.write("")
#op8 = pytrend.build_payload(kw_list=["Life Below Water"])

st.write("")

with st.beta_expander("Read about the SDG",expanded=False):
    st.subheader('Goal Description')
    st.write("The SDGs can only be realized with strong global partnerships and cooperation.")
    st.text("")
    st.write("A successful development agenda requires inclusive partnerships — at the global, regional, national and local levels — built upon principles and values, and upon a shared vision and shared goals placing people and the planet at the centre.")
    st.text("")
    st.write("Many countries require Official Development Assistance to encourage growth and trade. Yet, aid levels are falling and donor countries have not lived up to their pledge to ramp up development finance.")
    st.text("")
    st.write("Due to the COVID-19 pandemic, the global economy is projected to contract sharply, by 3 per cent, in 2020, experiencing its worst recession since the Great Depression.")
    st.text("")
    st.write("Strong international cooperation is needed now more than ever to ensure that countries have the means to recover from the pandemic, build back better and achieve the Sustainable Development Goals.")
    st.text("")





st.text("")
st.subheader("Please rate the following facts:")
st.text("")

st.write("(i) Development assistance is financial assistance from the richest to the poorest countries")
q49 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="49")

st.write("(ii) Since 2009, the number of web users in the developing countries has more than doubled")
q50 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="50")

st.write("(iii) EUR 800 billion is diverted each year from the developing countries to the countries of the north")
q51 = st.slider('Rate this on a scale from 1 to 5', 0, 5, key="51")

arr17 = np.array([q49, q50, q51])


with st.beta_expander("What are some of the ways to get involved?"):
            st.write("""Please follow the link below to know some of the partnering organizations that are actively contributing to this goal.""")
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
        st.title("Your top 3 recommendations are:")
        #st.write(indices[0])
        user1 = indices[0][0]
        user2 = indices[0][1]
        user3 = indices[0][2]

        #st.write(user1)
        #st.write(user2)
        #st.write(user3)

        
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


        st.write(fo1)
        st.write("")
        st.write(fo2)
        st.write("")
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

        














