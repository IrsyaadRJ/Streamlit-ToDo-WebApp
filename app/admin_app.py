import streamlit as st
from streamlit_option_menu import option_menu
from admin_app_func import *

# ToDO Application with CRUD functionality.
# Stored/retrieved the data inside the mysql.
# that is located in other server.
# @ Author : Irsyaad Rijwan.

# Initialized Horizontal Menu with.
# options menu that have its unique icons.
# Options : Create, Read, Update, Delete, About.
# @ return option_menu object.
def horizontal():
  selected = option_menu(
      menu_title = None,
      # menu options,
      options = ["About","Statistics", "Delete User"],
      # menu icons
      icons = ["info-circle","graph-up-arrow","trash"],
      # change the default icon of the menu title
      menu_icon = "cast",
      default_index = 0, # index of the icon 0 for menu title
      orientation = "horizontal", # orientation of the menu
      # css styles for the menu.
       styles={
        "container": {"padding": "0!important"},
      }
    )
  return selected

# Invoked when the logout button is clicked
# set the loggedIn state to False
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False

# Display the logout button.
def show_logout_button(login_url):
  st.button (f"Logout", on_click=LoggedOut_Clicked)
  go_to_login_page(login_url)

# Navigate to the login page
def go_to_login_page(login_url):
  if not st.session_state['loggedIn']:
    nav_to(login_url)

#  A function that displays the menu functionality,
#   when the user clicks one of the menu buttons.
def menu_func(option_menu):
  # URL of the first web app.
  login_url = "http://localhost:8081"
  # set the loggedIn state to True
  if 'loggedIn' not in st.session_state:
      st.session_state['loggedIn'] = True
  # Invoked the function when the user clicks on the menu.
  if option_menu == "About":
    option_about("Admin")
  if option_menu == "Statistics":
    option_statistics()
  if option_menu == "Delete User":
    option_delete()
  #Display the logout button
  show_logout_button(login_url)


  