from db_mysql_init import Base, Tasktable, User,engine
from db_mysql_func import (
  add_user,add_task,create_all_tables,delete_table,
  has_table
)
from datetime import date,timedelta


# Only create all tables and initialize, 
# if the tables are not created.
if not has_table(User,engine) and not has_table(Tasktable,engine):
  # Create all tables in the metadata to database.
  create_all_tables(Base,engine)
  #Initialize all users
  add_user("Admin","admin","admin","admin@gmail.com")
  add_user("Irsyaad Rijwan","blank404","blank404","blankid255@gmail.com")
  add_user("Big G","biggie","biggie","biggie@gmail.com")

  #Initialize the user's tasks.
  add_task("Reading a book", "Doing", date.today(),"blank404")
  add_task("COSC349 AS1", "Done", date.today(),"blank404")
  add_task("Hello World", "Doing", date.today(),"blank404")
  add_task("Watch a movie", "ToDo", date.today() + timedelta(days=4),"blank404")

  add_task("Math homework", "Doing", date.today() + timedelta(days=1),"biggie")
  add_task("Physic homework", "Doing", date.today() + timedelta(days=2),"biggie")
  add_task("Chemistry homework", "ToDo", date.today() + timedelta(days=4),"biggie")
  add_task("Go to park", "ToDo", date.today() + timedelta(days=4),"biggie")
  add_task("Clean my bedroom", "ToDo", date.today() + timedelta(days=3),"biggie")

