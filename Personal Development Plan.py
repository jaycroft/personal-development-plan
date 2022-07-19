import pandas as pd
import streamlit as st
from PIL import Image
from questions import communication_questions, time_mgmt_questions

tech_skills_select = ('Basic', 'Intermediate', 'Advanced')

response_list = ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always')

all_skills = ["Active Listening","Empathy","Data Visualization Tools","SQL","Python","Git","Hiring","Coaching"
            ,"Machine Leaning","JSON","HTML","Linux","Presentation","Prioritization","Critical Thinking","Statistics"
            ,"Data Cleaning","Data Analysis","Problem Solving","Algebra","Calculus","Data Warehousing"
            ,"Project Management","Time Management","Collaboration","Web Development","APIs","Database Systems"
            ,"Amazon Web Services (AWS)","Apache Airflow","Apache Spark","MySQL","Microsoft SQL Server","PostgreSQL"
            ,"Hadoop","Apache Kafka","Computer Vision","Natural Language Processing","Amazon Redshift","Deep Learning"
            ,"Data Manipulation","Big Data","Feature Selection","Regression Analysis","NoSQL","Model Deployment"
            ,"Tensorflow","Database Management","Spreadsheets","DevOps"]

all_skills.sort()

image = Image.open('logo/ufirst_full-on-ltgray.png')
st.image(image,width=500)
st.title('Personal Development Plan Assessment')


# def main_page():

role = st.selectbox('Role', ('Data Analyst/BI Analyst', 'Data Engineer', 'Data Scientist'))

technical_expander = st.expander("Technical Skills")
if role == 'Data Analyst/BI Analyst':
    data_analyst = []
    technical_expander.subheader('Technical Skills')
    python = technical_expander.radio('Data Visualization', tech_skills_select, horizontal=True)
    sql = technical_expander.radio('SQL', tech_skills_select, horizontal=True)
    git = technical_expander.radio('Git', tech_skills_select, horizontal=True)

    data_analyst.append(['Data Visualization', python])
    data_analyst.append(['SQL', sql])
    data_analyst.append(['Git', git])

    data_engineer_df = pd.DataFrame(data_analyst, columns=['Skill', 'Response'])
    technical_expander.write(data_engineer_df)

if role == 'Data Engineer':
    data_engineer = []
    technical_expander.subheader('Technical Skills')
    python = technical_expander.radio('Python', tech_skills_select, horizontal=True)
    sql = technical_expander.radio('SQL', tech_skills_select, horizontal=True)
    git = technical_expander.radio('Git', tech_skills_select, horizontal=True)
    data_engineer.append(['Python',python])
    data_engineer.append(['SQL', sql])
    data_engineer.append(['Git', git])

    data_engineer_df = pd.DataFrame(data_engineer,columns=['Skill','Response'])
    technical_expander.write(data_engineer_df)






communication_expander = st.expander("Communication Skills")
communication_expander.header('Communication Skills')
comm = []
communication_expander.markdown("##### "+communication_questions.q1)
communication1 = communication_expander.radio("Response",response_list, horizontal=True,key=0)
communication_expander.markdown("##### "+communication_questions.q2)
communication2 = communication_expander.radio("Response",response_list, horizontal=True,key=1)
communication_expander.markdown("##### "+communication_questions.q3)
communication3 = communication_expander.radio("Response",response_list, horizontal=True,key=2)
communication_expander.markdown("##### "+communication_questions.q4)
communication4 = communication_expander.radio("Response",response_list, horizontal=True,key=3)
communication_expander.markdown("##### "+communication_questions.q5)
communication5 = communication_expander.radio("Response",response_list, horizontal=True,key=4)
communication_expander.markdown("##### "+communication_questions.q6)
communication6 = communication_expander.radio("Response",response_list, horizontal=True,key=5)
communication_expander.markdown("##### "+communication_questions.q7)
communication7 = communication_expander.radio("Response",response_list, horizontal=True,key=6)
communication_expander.markdown("##### "+communication_questions.q8)
communication8 = communication_expander.radio("Response",response_list, horizontal=True,key=7)
communication_expander.markdown("##### "+communication_questions.q9)
communication9 = communication_expander.radio("Response",response_list, horizontal=True,key=8)
communication_expander.markdown("##### "+communication_questions.q10)
communication10 = communication_expander.radio("Response",response_list, horizontal=True,key=9)
communication_expander.markdown("##### "+communication_questions.q11)
communication11 = communication_expander.radio("Response",response_list, horizontal=True,key=10)
communication_expander.markdown("##### "+communication_questions.q12)
communication12 = communication_expander.radio("Response",response_list,horizontal=True,key=11)
communication_expander.markdown("##### "+communication_questions.q13)
communication13 = communication_expander.radio("Response",response_list,horizontal=True,key=12)
communication_expander.markdown("##### "+communication_questions.q14)
communication14 = communication_expander.radio("Response",response_list,horizontal=True,key=13)

comm.append([communication_questions.q1, communication1, 'Empathy'])
comm.append([communication_questions.q2, communication2, 'Presentation'])
comm.append([communication_questions.q3, communication3, 'Body Language'])
comm.append([communication_questions.q4, communication4, 'Empathy'])
comm.append([communication_questions.q5, communication5, 'Presentation'])
comm.append([communication_questions.q6, communication6, 'Body Language'])
comm.append([communication_questions.q7, communication7, 'Presentation'])
comm.append([communication_questions.q8, communication8, 'Empathy'])
comm.append([communication_questions.q9, communication9, 'Empathy'])
comm.append([communication_questions.q10, communication10, 'Clarification'])
comm.append([communication_questions.q11, communication11, 'Clarification'])
comm.append([communication_questions.q12, communication12, 'Presentation'])
comm.append([communication_questions.q13, communication13, 'Active Listening'])
comm.append([communication_questions.q14, communication14, 'Active Listening'])
comm_df = pd.DataFrame(comm, columns=['Question', 'Response', 'Category'])
comm_df['Numeric Value'] = comm_df['Response'].map({'Always': 1, 'Almost Always': 2, 'Sometimes': 3, 'Almost Never': 4, 'Never': 5})
# communication_expander.write(comm_df)
# communication_expander.markdown("## Score: "+str(comm_df['Numeric Value'].sum()))



time_mgmt_expander = st.expander("Time Management Skills")
time_mgmt_expander.subheader('Time Management Skills')
time_mgmt = []
time1 = time_mgmt_expander.radio(time_mgmt_questions.q1, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always',),horizontal=True)
time2 = time_mgmt_expander.radio(time_mgmt_questions.q2, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time3 = time_mgmt_expander.radio(time_mgmt_questions.q3, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time4 = time_mgmt_expander.radio(time_mgmt_questions.q4, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time5 = time_mgmt_expander.radio(time_mgmt_questions.q5, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time6 = time_mgmt_expander.radio(time_mgmt_questions.q6, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time7 = time_mgmt_expander.radio(time_mgmt_questions.q7, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time8 = time_mgmt_expander.radio(time_mgmt_questions.q8, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time9 = time_mgmt_expander.radio(time_mgmt_questions.q9, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time10 = time_mgmt_expander.radio(time_mgmt_questions.q10, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time11 = time_mgmt_expander.radio(time_mgmt_questions.q11, ('Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always'),horizontal=True)
time_mgmt.append([time_mgmt_questions.q1, time1, 'Awareness'])
time_mgmt.append([time_mgmt_questions.q2, time2, 'Planning'])
time_mgmt.append([time_mgmt_questions.q3, time3, 'Prioritization'])
time_mgmt.append([time_mgmt_questions.q4, time4, 'Prioritization'])
time_mgmt.append([time_mgmt_questions.q5, time5, 'Prioritization'])
time_mgmt.append([time_mgmt_questions.q6, time6, 'Prioritization'])
time_mgmt.append([time_mgmt_questions.q7, time7, 'Planning'])
time_mgmt.append([time_mgmt_questions.q8, time8, 'Awareness'])
time_mgmt.append([time_mgmt_questions.q9, time9, 'Execution'])
time_mgmt.append([time_mgmt_questions.q10, time10, 'Planning'])
time_mgmt.append([time_mgmt_questions.q11, time11, 'Prioritization'])
time_df = pd.DataFrame(time_mgmt, columns=['Question', 'Response', 'Category'])
time_df['Numeric Value'] = time_df['Response'].map({'Always': 1, 'Almost Always': 2, 'Sometimes': 3, 'Almost Never': 4, 'Never': 5})
# time_mgmt_expander.write(time_df)





career_expander = st.expander("Career")
future_role = career_expander.text_input("What role do you see yourself in 5 years down the road?")
skills_needed = career_expander.multiselect("What skills do you think you need to develop for your next role?",all_skills)



scores = "\n\nCOMMUNICATION: "+ str(comm_df['Numeric Value'].sum())+ "\n\nTIME MANAGEMENT: "+ str(time_df['Numeric Value'].sum()) +"SCORING:\n11-24 Excellent\n25-31 Good\n32+ Poor"
comm_file = comm_df.to_csv(index=None).encode('utf-8')
time_file = time_df.to_csv(index=None).encode('utf-8')


# with open('myfile.zip', 'rb') as f:
#    st.download_button('Download Zip', f, file_name='archive.zip')

st.download_button(
    label="Download Report",
    data=scores,
    file_name='Report.txt',
    mime='text/csv',
)

st.download_button(
    label="Download Communication Results",
    data=comm_file,
    file_name='Communication.csv',
    mime='text/csv',
)

st.download_button(
    label="Download Time Management Results",
    data=time_file,
    file_name='Time Management.csv',
    mime='text/csv',
)

