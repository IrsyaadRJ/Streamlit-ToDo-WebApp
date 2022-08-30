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

