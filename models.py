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

# --- Case Table ---
class Case(Base):
    __tablename__ = "cases"
    case_id = Column(Integer, primary_key=True, autoincrement=True)
    case_name = Column(String(256), nullable=False)
    case_type = Column(String(128), nullable=False)
    description = Column(Text)
    status = Column(String(32), nullable=False, default='Not Started')
    start_date = Column(DateTime, nullable=True)
    completed_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

# --- Task Table ---
class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    case_id = Column(Integer, ForeignKey('cases.case_id'), nullable=False)
    task_name = Column(String(256), nullable=False)
    description = Column(Text)
    status = Column(String(32), nullable=False, default='Not Started')
    due_date = Column(DateTime)
    day_offset = Column(Integer)
    documents_required = Column(Text)
    task_start_date = Column(DateTime)
    task_completed_date = Column(DateTime)
    last_updated_by = Column(String(64))
    last_updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    case = relationship('Case')

# --- TemplateType Table ---
class TemplateType(Base):
    __tablename__ = "template_types"
    template_type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(128), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())

# --- TaskTemplate Table (missing before!) ---
class TaskTemplate(Base):
    __tablename__ = "task_templates"
    task_template_id = Column(Integer, primary_key=True, autoincrement=True)
    template_type_id = Column(Integer, ForeignKey('template_types.template_type_id'), nullable=False)
    task_sequence = Column(Integer, nullable=False)
    task_name = Column(String(256), nullable=False)
    default_status = Column(String(32), nullable=False, default='Not Started')
    day_offset = Column(Integer)
    documents_required = Column(Text)

# --- TaskAttachment Table ---
class TaskAttachment(Base):
    __tablename__ = "task_attachments"
    attachment_id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('tasks.task_id'), nullable=False)
    original_filename = Column(String(256), nullable=False)
    stored_filename = Column(String(256), nullable=False)
    uploaded_by = Column(String(64))
    upload_timestamp = Column(DateTime, server_default=func.now())  # renamed for consistency with queries.py

# --- Remark Table (case_remarks for consistency with queries.py) ---
class CaseRemark(Base):
    __tablename__ = "case_remarks"
    remark_id = Column(Integer, primary_key=True, autoincrement=True)
    case_id = Column(Integer, ForeignKey('cases.case_id'), nullable=False)
    user_name = Column(String(64))
    message = Column(Text)
    timestamp = Column(DateTime, server_default=func.now())

