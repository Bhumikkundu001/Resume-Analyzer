import streamlit as st
import pandas as pd
import base64
import datetime
import plotly.express as px
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=st.secrets["db"]["host"],
        database=st.secrets["db"]["database"],
        user=st.secrets["db"]["user"],
        password=st.secrets["db"]["password"],
        port=st.secrets["db"]["port"]
    )

def get_table_download_link(df, filename, text):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

def insert_data(conn, name, email, resume_score, timestamp, total_page, predicted_field,
                user_level, actual_skills, recommended_skills, recommended_courses):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_data (Name, Email, Resume_Score, Timestamp, Total_Page,
        Predicted_Field, User_Level, Actual_Skills, Recommended_Skills, Recommended_Course)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, email, resume_score, timestamp, total_page, predicted_field,
          user_level, actual_skills, recommended_skills, recommended_courses))
    conn.commit()

def analyze_resume():
    # Dummy function, replace with your actual resume analysis logic
    return {
        'name': 'John Doe',
        'email': 'john@example.com',
        'score': 85,
        'pages': 2,
        'predicted_field': 'Data Science',
        'user_level': 'Intermediate',
        'actual_skills': 'Python, ML',
        'recommended_skills': 'NLP, Deep Learning',
        'recommended_courses': 'Coursera ML, FastAI'
    }

def run():
    st.title("Resume Analyzer")

    menu = ["User", "Admin"]
    choice = st.sidebar.selectbox("Login", menu)

    if choice == "User":
        st.subheader("Upload Your Resume")
        file = st.file_uploader("Upload", type=["pdf"])

        if st.button("Analyze") and file is not None:
            resume_data = analyze_resume()
            conn = get_connection()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            insert_data(
                conn,
                resume_data['name'],
                resume_data['email'],
                str(resume_data['score']),
                timestamp,
                resume_data['pages'],
                resume_data['predicted_field'],
                resume_data['user_level'],
                resume_data['actual_skills'],
                resume_data['recommended_skills'],
                resume_data['recommended_courses']
            )
            st.success("Resume processed and data saved!")

    else:
        st.success('Welcome to Admin Side')
        ad_user = st.text_input("Username")
        ad_password = st.text_input("Password", type='password')

        if st.button('Login'):
            if ad_user == 'admin_bhumik' and ad_password == '198200':
                st.success("Welcome Bhumik")
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute('''SELECT * FROM user_data''')
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['ID', 'Name', 'Email', 'Resume Score', 'Timestamp', 'Total Page',
                                                 'Predicted Field', 'User Level', 'Actual Skills', 'Recommended Skills',
                                                 'Recommended Course'])
                st.dataframe(df)
                st.markdown(get_table_download_link(df, 'User_Data.csv', 'Download Report'), unsafe_allow_html=True)

                plot_data = pd.read_sql('SELECT * FROM user_data;', conn)

                # Pie chart 1: Predicted Field
                field_labels = plot_data["Predicted_Field"].unique()
                field_values = plot_data["Predicted_Field"].value_counts()
                st.subheader("📈 Pie-Chart for Predicted Field Recommendations")
                fig = px.pie(plot_data, values=field_values, names=field_labels,
                             title='Predicted Field according to the Skills')
                st.plotly_chart(fig)

                # Pie chart 2: User Level
                level_labels = plot_data["User_Level"].unique()
                level_values = plot_data["User_Level"].value_counts()
                st.subheader("📈 Pie-Chart for User's👨‍💻 Experienced Level")
                fig = px.pie(plot_data, values=level_values, names=level_labels,
                             title="Pie-Chart📈 for User's👨‍💻 Experienced Level")
                st.plotly_chart(fig)
            else:
                st.error("Wrong ID & Password Provided")

run()