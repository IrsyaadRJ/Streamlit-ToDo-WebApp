import pandas as pd
from sqlalchemy import inspect
from db_mysql_init import Session, Tasktable, User

"""
  Check whether the table exists in the database.
  @return True if the table exists, False otherwise.
"""
def has_table(table,engine):
  insp = inspect(engine)
  return insp.has_table(table.__tablename__,None)

  """
    * Create database schema for all tables 
      that are stored in the base metadata.
    * By default checkfirst is set to True, 
      don’t issue CREATEs for tables already present in the target 
  """
def create_all_tables(Base,engine):
  Base.metadata.create_all(engine,checkfirst=True)

  """
    * Delete a specific table from the database
    * By default checkfirst is set to False, 
        don’t issue DROPs for tables that are not present in database.
  """
def delete_table(table,engine):
  table.__table__.drop(engine,checkfirst = True)
  
  """
    Check if the user is already registered.
    @return True if the user is already registered, False otherwise.
  """
def user_exists(username):
  local_session = Session()  # make a connection to the engine using session maker
  user_object = local_session.query(User).filter_by(username=username).first()
  local_session.close()
  if user_object is None:
    return False
  return True

  """
    Check if the email address is already registered.
    @return True if the email address is already registered, False otherwise.
  """
def email_exists(email):
  local_session = Session()  # make a connection to the engine using session maker
  email_object = local_session.query(User).filter_by(email=email).first()
  local_session.close()
  if email_object is None:
    return False
  return True

"""
    Check if the username and password are correct.
    @return True if username and password are correct. False otherwise.
  """
def login(username, password):
  local_session = Session()  # make a connection to the engine using session maker
  user_object = local_session.query(User).filter_by(
    username=username, password=password).first()
  local_session.close()
  if user_object is None:
    return False
  return True

  """
    Add the user details to the database.
  """
def add_user(name,username,password,email):
  local_session = Session() # make a connection to the engine using session maker
  new_user = User(name = name, username = username, 
                  password = password, email = email)
  local_session.add(new_user) # add the user to the session
  local_session.commit() # commit the session
  local_session.close()
  
  """
    Get the user object based on its username.
  """
def get_userObj(username):
  local_session = Session() 
  user_obj = local_session.query(User).filter_by(username=username)
  local_session.close()
  return user_obj
  
  """
    Get then name of the user.
  """
def get_name(user_obj):
  for record in user_obj:
    return record.name
  
  """
    Get the user's id based on its object.
  """
def get_user_id(user_obj):
  for record in user_obj:
    return record.id
"""
    Get the user's usersname based on its object.
"""
def get_username(user_obj):
  for record in user_obj:
    return record.username
"""
  Get the user instance based on its username.
  To link the tasks that is created by the user. 
"""
def get_author(username):
  local_session = Session() 
  user_obj = local_session.query(User).filter_by(username=username).first()
  local_session.close()
  return user_obj

"""
  Read the entire table and transform it into a data frame
  @return dataframe
"""
def read_entire_table(table,engine):
  df = pd.read_sql(f'SELECT * FROM {table.__tablename__}', engine) 
  return df 

"""
  Read the entire table and transform it into a data frame.
  Based on the user's id.
  @return dataframe
"""
def read_user_tasks(user_id, table, engine):
  df = pd.read_sql(f'''SELECT * FROM {table.__tablename__} 
                   WHERE user_id = {user_id}''', engine)
  return df 

"""
  Add the task and its author to the database.
"""
def add_task(task, task_status,task_due_date,username):
  local_session = Session() # make a connection to the engine using session maker
  author = local_session.query(User).filter_by(username=username).first()
  new_task = Tasktable(task = task, task_status = task_status,
                       task_due_date = task_due_date, author = author)
  local_session.add(new_task) # add the task to the session
  local_session.commit() # commit the session