from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API key for Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to read SQL query results from the database
def read_sql_query(sql, db_path):
    con = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql, con)
    con.close()
    return df

# Function to get database schema as a DataFrame
def get_db_schema_df(db_path):
    schema_data = []
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Get all table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cur.fetchall()]
    # Get columns for each table
    for table in tables:
        cur.execute(f"PRAGMA table_info({table});")
        columns = cur.fetchall()
        for col in columns:
            schema_data.append({"Table": table, "Column": col[1], "Data Type": col[2]})
    con.close()
    # Convert to DataFrame
    return pd.DataFrame(schema_data)

# Streamlit app configuration
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.title("Prompt To SQL Data")
st.header("Convert your Prompts to get responses, NO need to learn DBMS 😎")

# User inputs: Database file and question
db_file = st.file_uploader("Upload your database", type="db")
question = st.text_input("Input your question:", key="input")

# Display the database schema in DataFrame format if the file is uploaded
if db_file:
    # Save the uploaded database file
    db_path = "temp_student.db"
    with open(db_path, "wb") as f:
        f.write(db_file.getbuffer())

    # Get and display database schema in DataFrame format
    schema_df = get_db_schema_df(db_path)
    st.subheader("Database Schema:")
    st.dataframe(schema_df)

    # Prompt for the Gemini model, dynamically updated with schema information
    prompt = [
        f"""
        You are an expert in converting English questions to SQL queries!
        Here is the database schema for reference:
        {', '.join([f'Table {row["Table"]} with columns {", ".join(schema_df[schema_df["Table"] == row["Table"]]["Column"].unique())}' for _, row in schema_df.iterrows()])}

        Use this schema information to accurately construct SQL queries based on the user question.
        
        Important:
        1. Do NOT include backticks (```) or the keyword "sql" in the SQL command output.
        2. Just return the plain SQL command without any markdown formatting.
        
        Example questions:
        - How many records are in the employee table?
        - Show all data for students in the 'Computer Science' course.
        - What are the names of customers who made a purchase in the last month?
        """
    ]

    # Process the question and show results when the submit button is clicked
    if st.button("Ask the question"):
        # Get SQL command from the Gemini model
        sql_command = get_gemini_response(question, prompt)
        
        # Fetch and display query results in a DataFrame
        response_df = read_sql_query(sql_command, db_path)
        st.subheader("The Response is")
        st.dataframe(response_df)
        
        # Clean up temporary database file
        os.remove(db_path)
