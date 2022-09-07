import streamlit as st
from login_page import main_login_page
from db_mysql_init import Base,engine
from db_mysql_func import create_all_tables
from admin_app import *

if __name__ == '__main__':
  # Display the admin interface
  menu_func(horizontal())