from sqlalchemy.orm import declarative_base,sessionmaker, relationship
from sqlalchemy import (create_engine, ForeignKey, 
                        Column, String, Date, 
                        DateTime, Integer, Text)
from datetime import date, datetime

# Make a connection to the database.
connection = "mysql+pymysql://{username}:{password}@{host}/{database}".format(
    username="webuser", password="insecure_db_pw", 
    host="192.168.56.12", database = "fvision")

# contains a metadata object where newly
# defined table objects are stored.
Base = declarative_base()

# Create an engine instance that connects to the database.
engine = create_engine(connection)

# Create a session and connect it to the database(engine instance).
Session = sessionmaker(bind=engine)

"""
    class User:
        id int
        username str
        password str
        name str
        email str
        tasks (author of the task)
        (one to many relationship between User table and Tasktable table)
"""
# Schema for the User table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(25), nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(40), nullable = True)
    tasks = relationship("Tasktable",backref="author", cascade = "all, delete",post_update=True)
    
    def __repr__(self):
        return f"< User id = {self.id} username = {self.username} name = {self.name} >"

"""
    class Paper:
        id int
        user_id int (foreign key)
        task TEXT
        task_status string
        task_due_date DATE
        date_created DATE
"""
# Schema for the Tasktable table.
class Tasktable(Base):
    # The name of the table
    __tablename__ = "tasktables"
    # By default auto-increment is set to True.
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    task = Column(Text(), nullable=False)
    task_status = Column(String(25), nullable=False)
    task_due_date = Column(Date())
    date_created = Column(Date(), default=date.today())

    # return string representation of the object
    def __repr__(self):
        return f"""< Tasktable id = {self.id} name = {self.name} 
                task = {self.task} task_status = {self.task_status} 
                task_due_date = {self.task_due_date} datetime_created = {self.date_created}>"""

