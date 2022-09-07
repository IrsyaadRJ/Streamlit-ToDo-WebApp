import streamlit as st
import plotly.express as px
import pandas as pd
from db_mysql_init import engine, Base, Tasktable,User
from db_mysql_func import (
  read_all_tasks,
  read_all_users, delete_user
)

# Using meta refresh to create an instant client-side redirect
def nav_to(url):
  nav_script = f"""
      <meta http-equiv="refresh" content="0;URL='{url}'"/>
  """
  st.write(nav_script, unsafe_allow_html=True)
  
# Create a layout for "About" menu
def option_about(name_of_user):
  st.title(f"Welcome {name_of_user}!!")
  st.header("Admin's Panel of ToDo Application")
  st.markdown("⭐ Select the 'Statistics' menu to see the interesting statistics of the user interaction with ToDo App")
  st.markdown("⭐ Select the 'Delete User' menu to delete the user.")

# Create a layout for "Statistics" menu
def option_statistics():
  st.subheader("View Items")
  # Get the table data frame
  table_df = read_all_tasks(Tasktable, engine)
  # Rename the columns of the data frame
  table_df.columns = ["ID", "User ID", "Task", "Status", "Due Date", "Date Created"]
  with st.expander("View All Tasks"):
    # Present the data frame
    st.write(table_df)
  with st.expander("View number of task per user"):
    task_df = table_df[["User ID","Task"]].value_counts().to_frame()
    task_df = task_df.reset_index()
    task_df.columns = ["User ID", "Task","Count"]
    # Create a pie chart
    plot = px.bar(task_df, x = "User ID", y = "Count")
    st.plotly_chart(plot)
    # Present the pie chart
  with st.expander("View Status Of All Tasks"):
    task_df = table_df["Status"].value_counts().to_frame()
    task_df = task_df.reset_index()
    task_df.columns = ["Status", "Count"]
    # Create a pie chart
    plot = px.pie(task_df, names = "Status", values = "Count")
    # Present the pie chart
    st.plotly_chart(plot)
  
# Create a layout for "Delete" menu
def option_delete():
  st.subheader("Delete user")
  st.warning("You cannot delete the admin !!")
  st.info("Only user's id and user's username will be presented !!")
  # Get the table data frame
  users_df = read_all_users(User,engine)
  # Get only the user's id and username column 
  updated_df = users_df[["id","username"]]
  with st.expander("View Current Users:"):
    # Present the data frame
    st.dataframe(updated_df)
  # iterate through the row(in tuple) and convert it to list
  list_df = [list(i) for i in updated_df.itertuples()]
  # Get list of user's username except admin.
  list_usernames = []
  for i in list_df:
    if i[2] != "admin":
      list_usernames.append((i[1],i[2])) 
  # Create select box layout to select the user
  selected_user = st.selectbox("Task to delete", list_usernames)
  #task id
  user_id = None
  username = None
  # Added if there is a user to be selected.
  if selected_user is not None:
    user_id = selected_user[0]
    username = selected_user[1]
  #Create a button to delete the user.
  if st.button("Delete User"):
    # Delete the task
    delete_user(user_id,username)
    st.success(f"User Has Been Successfully Deleted")
    # Show the updated tasks
    with st.expander("View Updated Users:"):
      new_df = read_all_users(User,engine)
      st.dataframe(new_df)
  