import streamlit as st
from login_page import main_login_page
from db_mysql_init import Base,engine
from db_mysql_func import create_all_tables

if __name__ == '__main__':
  # Create the tables if they don't exist.'
  create_all_tables(Base,engine)
  # Show the login page of the web app.
  # To login to the web app
  # and to interact with the web app.
  main_login_page()