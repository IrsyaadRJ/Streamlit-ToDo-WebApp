import streamlit as st
import plotly.express as px
from db_mysql_init import engine, Base, Tasktable
from db_mysql_func import (add_task,read_entire_table,
                           read_user_tasks,
                           get_username)
# "Create" option layout
def option_create(user_obj):
  username = get_username(user_obj)
  #Subheader
  st.subheader("Add Items")
  #Layout
  col1,col2 = st.columns(2)
  with col1:
    # get the tasks
    task = st.text_area("Task To Do")
  with col2:
    #get the status and due date
    list_status = [" ToDo","Doing","Done"]
    task_status = st.selectbox("Status",list_status)
    task_due_date = st.date_input("Due Date")
  if st.button("Add Task"):
    # added to database
    add_task(task, task_status, task_due_date,username)
    st.success(f"Successfully Added Task: {task}")

def option_read(user_id):
  st.subheader("View Items")
  # Get the table data frame
  table_df = read_user_tasks(user_id, Tasktable, engine)
  # Rename the columns of the data frame
  table_df.columns = ["ID", "User ID", "Task", "Status", "Due Date", "Date Created"]
  # Present the data frame
  st.write(table_df)
  with st.expander("Task Status"):
    task_df = table_df["Status"].value_counts().to_frame()
    task_df = task_df.reset_index()
    task_df.columns = ["Status", "Count"]
    # Present the dataframe that contains the user's tasks.
    st.dataframe(task_df)
    # Create a pie chart
    plot1 = px.pie(task_df, names = "Status", values = "Count")
    # Present the pie chart
    st.plotly_chart(plot1)

  