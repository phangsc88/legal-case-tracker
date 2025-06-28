# models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, func, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()

# --- User Table ---
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    privilege = Column(String(16), nullable=False, default='User')
    created_at = Column(DateTime, server_default=func.now())

    # For relationship with cases/tasks if you need
    # cases = relationship('Case', back_populates='user')

# --- Case Table ---
class Case(Base):
    __tablename__ = "cases"
    case_id = Column(Integer, primary_key=True, autoincrement=True)
    case_name = Column(String(256), nullable=False)  # <-- change here!
    description = Column(Text)
    status = Column(String(32), nullable=False, default='Not Started')
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Example: assigned_to = Column(Integer, ForeignKey('users.user_id'))
    # user = relationship('User', back_populates='cases')

# --- Task Table ---
class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    case_id = Column(Integer, ForeignKey('cases.case_id'), nullable=False)
    title = Column(String(256), nullable=False)
    description = Column(Text)
    status = Column(String(32), nullable=False, default='Not Started')
    due_date = Column(DateTime)
    completed_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    case = relationship('Case')

# --- Example: Add more tables as needed ---
# class Document(Base):
#     __tablename__ = "documents"
#     document_id = Column(Integer, primary_key=True, autoincrement=True)
#     case_id = Column(Integer, ForeignKey('cases.case_id'), nullable=False)
#     file_path = Column(String(512), nullable=False)
#     uploaded_at = Column(DateTime, server_default=func.now())
#     case = relationship('Case')

# --- TemplateType Table ---
class TemplateType(Base):
    __tablename__ = "template_types"
    template_type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(128), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())

# --- TaskAttachment Table ---
class TaskAttachment(Base):
    __tablename__ = "task_attachments"
    attachment_id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('tasks.task_id'), nullable=False)
    original_filename = Column(String(256), nullable=False)
    stored_filename = Column(String(256), nullable=False)
    uploaded_by = Column(String(64))
    uploaded_at = Column(DateTime, server_default=func.now())

# --- Remark Table ---
class Remark(Base):
    __tablename__ = "remarks"
    remark_id = Column(Integer, primary_key=True, autoincrement=True)
    case_id = Column(Integer, ForeignKey('cases.case_id'), nullable=False)
    user_name = Column(String(64))
    message = Column(Text)
    created_at = Column(DateTime, server_default=func.now())