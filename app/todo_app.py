import streamlit as st
from streamlit_option_menu import option_menu
from todo_app_func import *
from db_mysql_func import (get_name,
                           get_user_id)

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
      options = ["About","Create", "Read", "Update", "Delete"],
      # menu icons
      icons = ["info-circle","pencil-square","book","gear","trash"],
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

#  A function that displays the menu functionality,
#   when the user clicks one of the menu buttons.
def menu_func(option_menu,user_obj):
  name_of_user = get_name(user_obj)
  user_id = get_user_id(user_obj)
  # Invoked the function when the user clicks on the menu.
  if option_menu == "Create":
    option_create(user_obj)
  if option_menu == "Read":
    option_read(user_id)
  if option_menu == "Update":
    option_update(user_id)
  if option_menu == "Delete":
    option_delete(user_id)
  if option_menu == "About":
    option_about(name_of_user)


# if __name__ == "__main__":
#   menu_func(horizontal())
  