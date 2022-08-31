import streamlit as st
from todo_app import *
from db_mysql_func import (
  add_user,
  user_exists,
  email_exists,
  login
)

# Set the logged in state to false, 
# when the user clicks the logout button.
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False

# Set the sign up state to true, 
# when the user clicks the sign up button.
def Signup_Clicked():
   st.session_state['signUp'] = True

# Set the sign up state to false, 
# when the user clicks the go back button.
# The user will be directed to the login page.
def back_from_signup():
  st.session_state['signUp'] = False

# Show the logout button to logout from the web app.
def show_logout_button(login_section,logout_section):
  login_section.empty()
  with logout_section:
    st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)

# When the user clicks the login in button,
# check whether the username and password 
#  that the user enters are matched
#  with the username and password in the database.
# If the username and password are matched,
#   then set the logged in state to True.
# False, otherwise, and show the error message.
def LoggedIn_Clicked(userName, password):
    if login(userName, password):
        st.session_state['loggedIn'] = True
    else:
      st.session_state['loggedIn'] = False;
      st.error("Invalid user name or password")

# Sign up form 
# The following input fields are going to be checked for validity/duplicated.
# new_name: The fullname of the user 
#   (Cannot be empty,must be alphabetical and cannot be less than 5 characters).
# new_username: The username of the user 
#   (Cannot be empty and cannot be less than 5 characters).
# new_user_email: The email address of the user.
#   (Cannot be empty and cannot be less than 5 characters).
# password: The password of the user 
#   (Cannot be empty and cannot be less than 5 characters).
# Add all user's details to the database
# username and email that are alredy registered cannot be entered twice.
def signup_form():
  new_name = st.text_input(label='Enter Your Name*')
  new_username = st.text_input(label='Enter Username*')
  new_user_email = st.text_input(label='Enter Email Address*')
  new_user_pas = st.text_input(label='Enter Password*', type='password')
  user_pas_conf = st.text_input(label='Confirm Password*', type='password')
  note = st.markdown('**required fields*')
  signup = st.form_submit_button(label='Sign Up')
  
  if signup:
    if '' in [new_name,new_username, new_user_email, new_user_pas]:
      st.error('Some fields are missing')
    else:
      if len(new_name) < 5 or new_name.isalpha():
        st.error("Please Enter your valid name !!")
      if len(new_username) < 5:
        st.error('Username must be at least 5 characters long')
      if len(new_user_email) < 5:
        st.error('Email must be at least 5 characters long')
      if len(new_user_pas) < 5:
        st.error('Password must be at least 5 characters long')
      if user_exists(new_username):
        st.error('Username already exists')
      if email_exists(new_user_email):
        st.error('Email is already registered')
      else:
        if new_user_pas != user_pas_conf:
          st.error('Passwords do not match')
        else:
          add_user(new_name,new_username,new_user_email,new_user_pas)
          st.success('You have successfully registered!')
          st.success("Please go back and logged in to your account!")
          del new_user_pas, user_pas_conf

# The login page layout
def show_login_page(login_section):
    with login_section:
      if st.session_state['loggedIn'] == False:
        userName = st.text_input (label="", value="", placeholder="Enter your user name")
        password = st.text_input (label="", value="",placeholder="Enter password", type="password")
        col1,col2 = st.columns(2)
        with col1:
          st.button (f"Login", on_click=LoggedIn_Clicked, args= (userName, password))
        with col2:
          st.button(f"Sign Up", on_click=Signup_Clicked)

# The sign up page layout
def show_signup_page(signup_section):
  with signup_section:
    with st.form("signup_form", clear_on_submit=True):
      signup_form()
    #go back button below the signup form
    go_back = st.button('Go Back', on_click = back_from_signup)
  
# The main login page layout.
# This is the function that will be called in the main module.
def main_login_page():
  # Initialize the containers layout
  header_section = st.container()
  login_section = st.container()
  signup_section = st.container()
  logout_section = st.container()
  with header_section:
    st.title("ToDo Application")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state and 'signUp' not in st.session_state:
      st.session_state['loggedIn'] = False
      st.session_state['signUp'] = False
      show_login_page(login_section) 
    else:
      if st.session_state['loggedIn']:
        show_logout_button(login_section,logout_section)    
        menu_func(horizontal())
      else:
        if st.session_state['signUp']:
          show_signup_page(signup_section)
        else:
          show_login_page(login_section)
          st.session_state['signUp'] = False