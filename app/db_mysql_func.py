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
  local_session.close()

  """
    Get a task based on its id and user's id (author).
    @return a dataframe contain the task details.
  """
def read_a_task(user_id,task_id, table, engine):
  df = pd.read_sql(f'''SELECT * FROM {table.__tablename__} 
                   WHERE user_id = {user_id} and id = {task_id}''', engine)
  return df 

  """
    Get a task object based on its id and user's id (author).
    @return task object.
  """
def get_taskObj(user_id,task_id):
  local_session = Session() 
  task_obj = local_session.query(Tasktable).filter_by(id = task_id,user_id=user_id).first()
  local_session.close()
  return task_obj

  """
   Get a task from its object.
  @return a task (string).
  """
def get_task(task_obj):
  return task_obj.task
  """
   Get a task's status from its object.
  @return a task'status (string).
  """
def get_task_status(task_obj):
   return task_obj.task_status
  """
   Get a task's due date from its object.
  @return a task (date object).
  """
def get_due_date(task_obj):
  return task_obj.task_due_date
  
  """
   Update a task'details based on its id and user's id (author). 
   The following details will be updated:
    - task (string).
    - task_status (string).
    - due_date (date).
  """
def update_task(user_id, task_id, task, task_status,task_due_date):
  local_session = Session() 
  curr_task = local_session.query(Tasktable).filter_by(id = task_id, user_id = user_id).first()
  curr_task.task = task
  curr_task.task_status = task_status
  curr_task.task_due_date = task_due_date
  local_session.commit() # commit the session
  local_session.close()
  """
   Delete a task based on its id and user's id (author).
  """
def delete_task(user_id,task_id):
  local_session = Session()
  curr_task = local_session.query(Tasktable).filter_by(id = task_id, user_id = user_id).first()
  local_session.delete(curr_task)
  local_session.commit()
  local_session.close()

"""
Check whether the user is admin or not.
@return True if the user is admin, False otherwise
"""
def is_admin(user_obj):
  if(get_username(user_obj) == "admin"):
    return True
  return False

"""
Get all tasks that have been created by all users.
@return df dataframe contains all tasks
"""
def read_all_tasks(table, engine):
  df = pd.read_sql(f'''SELECT * FROM {table.__tablename__}''', engine)
  return df 

"""
Gel all users in the database.
@return df dataframe all users' details.
"""
def read_all_users(table, engine):
  df = pd.read_sql(f'''SELECT * FROM {table.__tablename__}''', engine)
  return df 

"""
Delete a user based on its user_id and username.
"""
def delete_user(user_id,username):
  local_session = Session()
  curr_user = local_session.query(User).filter_by(id = user_id, username = username).first()
  print(curr_user)
  local_session.delete(curr_user)
  local_session.commit()
  local_session.close()

  