import streamlit as st
import plotly.express as px
from db_mysql_init import engine, Base, Tasktable
from db_mysql_func import (
  add_task,read_entire_table,
  read_user_tasks,get_username,
  get_taskObj, get_task,
  get_task_status,get_due_date,
  update_task,delete_task
  )

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

# Create a layout for "Update" menu
def option_update(user_id):
  st.subheader("Edit/ Update Items")
  # Get the table data frame
  table_df = read_user_tasks(user_id, Tasktable, engine)
  # Rename the columns of the data frame
  table_df.columns = ["ID", "User ID", "Task", "Status", "Due Date", "Date Created"]
  
  # Expand to see
  with st.expander("View Current Tasks:"):
    # Present the data frame
    st.dataframe(table_df)
    
  # Get subset of the data frame
  updated_df = table_df[["ID","Task","Status"]]
  # iterate through the row(in tuple) and convert it to list
  list_df = [list(i) for i in updated_df.itertuples()]
  # Get list of tuple that contains the id of the task and the task it self.
  list_tasks = [(i[1], i[2], i[3]) 
                for i in list_df]
  # Create select box layout to select the task
  selected_task = st.selectbox("Task to edit", list_tasks)
  # the task id
  task_id = None
  # Added if there is a task to be selected.
  if selected_task is not None:
    task_id = selected_task[0]
    
  if selected_task:
    # Get the task object
    selected_result = get_taskObj(user_id,task_id)
    task = get_task(selected_result)
    task_status = get_task_status(selected_result)
    task_due_date = get_due_date(selected_result)
    #Layout
    col1,col2 = st.columns(2)
    with col1:
      task = st.text_area("Current Task To Do",task)
    with col2:
      list_status = [" ToDo","Doing","Done"]
      curr_status_index = list_status.index(task_status)
      task_status = st.selectbox("Current Task Status",
                                 list_status,index=curr_status_index)
      task_due_date = st.date_input("Current Due Date",task_due_date)
    # Create a button to update the task
    if st.button("Update Task"):
      is_error = False
      if(len(task) < 1):
        st.error("Task cannot be empty !")
        is_error = True
      else:
        update_task(user_id,task_id,task, task_status, task_due_date)
        st.success(f"Successfully Updated The Task")
        is_error = False
      # Show the updated tasks
      if not is_error:
        with st.expander("View Updated Tasks:"):
          new_df = read_user_tasks(user_id, Tasktable, engine)
          new_df.columns = ["ID", "User ID", "Task", "Status", "Due Date", "Date Created"]
          st.dataframe(new_df)
          
# Create a layout for "Delete" menu
def option_delete(user_id):
  st.subheader("Delete Item")
  # Get the table data frame
  table_df = read_user_tasks(user_id, Tasktable, engine)
  # Rename the columns of the data frame
  table_df.columns = ["ID", "User ID", "Task", "Status", "Due Date", "Date Created"]
  with st.expander("View Current Tasks:"):
    # Present the data frame
    st.dataframe(table_df)
  # Get subset of the data frame
  updated_df = table_df[["ID","Task","Status"]]
  # iterate through the row(in tuple) and convert it to list
  list_df = [list(i) for i in updated_df.itertuples()]
  # Get list of tuple that contains the id of the task and the task it self.
  list_tasks = [(i[1], i[2], i[3]) 
                for i in list_df]
  # Create select box layout to select the task
  selected_task = st.selectbox("Task to delete", list_tasks)
  #task id
  task_id = None
  # Added if there is a task to be selected.
  if selected_task is not None:
    task_id = selected_task[0]
  #Create a button to delete the task.
  if st.button("Delete Task"):
    # Delete the task
    delete_task(user_id,task_id)
    st.success(f"Task Has Been Successfully Deleted")
    # Show the updated tasks
    with st.expander("View Updated Tasks:"):
      new_df = read_user_tasks(user_id, Tasktable, engine)
      new_df.columns = ["ID", "User ID", "Task", "Status", "Due Date", "Date Created"]
      st.dataframe(new_df)

# Create a layout for "About" menu
def option_about(name_of_user):
  st.title(f"Welcome {name_of_user}!!")
  st.header("ToDo Application")
  st.markdown("⭐ Select the 'Create' menu to create a new task")
  st.markdown("⭐ Select the 'Read' menu to see the table of tasks that you'd created")
  st.markdown("⭐ Select the 'Update' menu to update a task")
  st.markdown("⭐ Select the 'Delete' menu to delete a task")

  