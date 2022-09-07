import streamlit as st
from login_page import main_login_page
from db_mysql_init import Base,engine

if __name__ == '__main__':
  # Show the login page of the web app.
  # To login to the web app
  # and to interact with the web app.
  main_login_page()