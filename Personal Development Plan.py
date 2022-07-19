import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
from questions import communication_questions, time_mgmt_questions, data_viz_questions

tech_skills_select = ('Basic', 'Intermediate', 'Advanced')

response_list = ['Always','Almost Always','Sometimes','Almost Never','Never']


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
# career_expander = st.expander("Career")
# future_role = st.text_input("What role do you see yourself in 5 years down the road?")
# skills_needed = st.multiselect("What skills do you think you need to develop for your next role?",all_skills)


technical_expander = st.expander("Technical Skills")
if role == 'Data Analyst/BI Analyst':
    data_analyst = []
    data_viz = []
    technical_expander.subheader('Data Visualization')
    technical_expander.caption('Match the chart goal with the appropriate chart type.')
    data_viz_1 = technical_expander.selectbox(data_viz_questions.q1, data_viz_questions.chart_types)
    data_viz_2 = technical_expander.selectbox(data_viz_questions.q2, data_viz_questions.chart_types)
    data_viz_3 = technical_expander.selectbox(data_viz_questions.q3, data_viz_questions.chart_types)
    data_viz_4 = technical_expander.selectbox(data_viz_questions.q4, data_viz_questions.chart_types)
    data_viz_5 = technical_expander.selectbox(data_viz_questions.q5, data_viz_questions.chart_types)
    data_viz_6 = technical_expander.selectbox(data_viz_questions.q6, data_viz_questions.chart_types)
    data_viz_7 = technical_expander.selectbox(data_viz_questions.q7, data_viz_questions.chart_types)
    data_viz_8 = technical_expander.selectbox(data_viz_questions.q8, data_viz_questions.chart_types)
    data_viz_9 = technical_expander.selectbox(data_viz_questions.q9, data_viz_questions.chart_types)
    data_viz_10 = technical_expander.selectbox(data_viz_questions.q10, data_viz_questions.chart_types)
    data_viz.append([data_viz_questions.q1, data_viz_1, data_viz_questions.a1])
    data_viz.append([data_viz_questions.q2, data_viz_2, data_viz_questions.a2])
    data_viz.append([data_viz_questions.q3, data_viz_3, data_viz_questions.a3])
    data_viz.append([data_viz_questions.q4, data_viz_4, data_viz_questions.a4])
    data_viz.append([data_viz_questions.q5, data_viz_5, data_viz_questions.a5])
    data_viz.append([data_viz_questions.q6, data_viz_6, data_viz_questions.a6])
    data_viz.append([data_viz_questions.q7, data_viz_7, data_viz_questions.a7])
    data_viz.append([data_viz_questions.q8, data_viz_8, data_viz_questions.a8])
    data_viz.append([data_viz_questions.q9, data_viz_9, data_viz_questions.a9])
    data_viz.append([data_viz_questions.q10, data_viz_10, data_viz_questions.a10])
    data_viz_df = pd.DataFrame(data_viz, columns=['Chart Goal', 'Response', "Answer"])
    data_viz_df[['Answer1', 'Answer2', 'Answer3']] = data_viz_df['Answer'].str.split(",", n=3, expand=True)
    data_viz_df.fillna(' ', inplace=True)
    data_viz_df.drop(columns='Answer', inplace=True)
    data_viz_df['Score'] = data_viz_df.apply(lambda x: 1 if x['Response'] in x['Answer1'] else (
        1 if x['Response'] in x['Answer2'] else (1 if x['Response'] in x['Answer3'] else 0)), axis=1)
    data_viz_score = str(data_viz_df['Score'].sum()/10*100.00)+'%'
    # data_viz_df['Match'] = data_viz_df['Response'].values().isin(data_viz_df['Answer1'].values())
    # technical_expander.write(data_viz_df)
    # technical_expander.write(data_viz_score)

    technical_expander.subheader('SQL')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=SQL")
    sql_score = technical_expander.text_input('Your SQL Quiz Score')

    technical_expander.subheader('Git')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=GIT")
    git_score = technical_expander.text_input('Your Git Quiz Score')

    technical_expander.subheader('Pandas')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=PANDAS")
    pandas_score = technical_expander.text_input('Your Pandas Quiz Score')

    data_analyst.append(['Data Visualization',data_viz_score])
    data_analyst.append(['SQL',sql_score])
    data_analyst.append(['Git',git_score])
    data_analyst.append(['Pandas',pandas_score])
    data_analyst_df = pd.DataFrame(data_analyst, columns=['Skill','Score'])
    technical_expander.write(data_analyst_df)

    da_file = data_analyst_df.to_csv(index=None)

    technical_expander.download_button(
        label="Download Report",
        data=da_file,
        file_name='Data Analyst - Technical Skill.csv',
        mime='text/csv',
    )



if role == 'Data Engineer':
    technical_expander.subheader('SQL')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=SQL")
    sql_score = technical_expander.text_input('Your SQL Quiz Score')

    technical_expander.subheader('Git')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=GIT")
    git_score = technical_expander.text_input('Your Git Quiz Score')

    technical_expander.subheader('Python')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON")
    python_score = technical_expander.text_input('Your Python Quiz Score')

    technical_expander.subheader('Pandas')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=PANDAS")
    pandas_score = technical_expander.text_input('Your Pandas Quiz Score')

if role == 'Data Scientist':
    technical_expander.subheader('SQL')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=SQL")
    sql_score = technical_expander.text_input('Your SQL Quiz Score')

    technical_expander.subheader('Git')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=GIT")
    git_score = technical_expander.text_input('Your Git Quiz Score')

    technical_expander.subheader('Pandas')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.asp?qtest=PANDAS")
    pandas_score = technical_expander.text_input('Your Pandas Quiz Score')

    technical_expander.subheader('SciPy')
    technical_expander.write("https://www.w3schools.com/quiztest/quiztest.php?qtest=SCIPY")
    pandas_score = technical_expander.text_input('Your SciPy Quiz Score')

# def communication():
communication_expander = st.expander("Communication Skills")
# communication_expander.header('Communication Skills')
comm = []
communication1 = communication_expander.radio(communication_questions.q1,response_list)
communication2 = communication_expander.radio(communication_questions.q2,response_list)
communication3 = communication_expander.radio(communication_questions.q3,response_list)
communication4 = communication_expander.radio(communication_questions.q4,response_list)
communication5 = communication_expander.radio(communication_questions.q5,response_list)
communication6 = communication_expander.radio(communication_questions.q6,response_list)
communication7 = communication_expander.radio(communication_questions.q7,response_list)
communication8 = communication_expander.radio(communication_questions.q8,response_list)
communication9 = communication_expander.radio(communication_questions.q9,response_list)
communication10 = communication_expander.radio(communication_questions.q10,response_list)
communication11 = communication_expander.radio(communication_questions.q11,response_list)
communication12 = communication_expander.radio(communication_questions.q12,response_list)
communication13 = communication_expander.radio(communication_questions.q13,response_list)
communication14 = communication_expander.radio(communication_questions.q14,response_list)
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
comm_file = comm_df.to_csv(index=None).encode('utf-8')
communication_expander.download_button(
    label="Download Communication Results",
    data=comm_file,
    file_name='Communication.csv',
    mime='text/csv',
)


# def time_management():
time_mgmt_expander = st.expander("Time Management Skills")
# time_mgmt_expander.subheader('Time Management Skills')
time_mgmt = []
time1 = time_mgmt_expander.radio(time_mgmt_questions.q1,response_list)
time2 = time_mgmt_expander.radio(time_mgmt_questions.q2,response_list)
time3 = time_mgmt_expander.radio(time_mgmt_questions.q3,response_list)
time4 = time_mgmt_expander.radio(time_mgmt_questions.q4,response_list)
time5 = time_mgmt_expander.radio(time_mgmt_questions.q5,response_list)
time6 = time_mgmt_expander.radio(time_mgmt_questions.q6,response_list)
time7 = time_mgmt_expander.radio(time_mgmt_questions.q7,response_list)
time8 = time_mgmt_expander.radio(time_mgmt_questions.q8,response_list)
time9 = time_mgmt_expander.radio(time_mgmt_questions.q9,response_list)
time10 = time_mgmt_expander.radio(time_mgmt_questions.q10,response_list)
time11 = time_mgmt_expander.radio(time_mgmt_questions.q11,response_list)
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

time_file = time_df.to_csv(index=None).encode('utf-8')
time_mgmt_expander.download_button(
    label="Download Time Management Results",
    data=time_file,
    file_name='Time Management.csv',
    mime='text/csv',
)




# def career():



# def Results ():
summary_report = "CURRENT ROLE: "+role\
                 +"\n\nFUTURE ROLE: " \
                 + str(comm_df)\
                 +"\n\nCOMMUNICATION SCORE: "+ str(comm_df['Numeric Value'].sum()) \
                 +"\n\nCOMMUNICATION SCORING:\n14-28 Excellent\n29-42 Good\n43-70 Needs Improvement\n"\
                 + str(time_df)\
                 +"\n\nTIME MANAGEMENT SCORE: "+ str(time_df['Numeric Value'].sum()) \
                 +"\n\nTIME MANAGEMENT SCORING:\n11-24 Excellent\n25-31 Good\n32+ Needs Improvement\n"\



# with open('myfile.zip', 'rb') as f:
#    st.download_button('Download Zip', f, file_name='archive.zip')

st.download_button(
    label="Download Summary Report",
    data=summary_report,
    file_name='Report.txt',
    mime='text/csv',
)





