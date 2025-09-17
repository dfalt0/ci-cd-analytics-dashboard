from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Build(Base):
    __tablename__ = "builds"
    id = Column(Integer, primary_key=True, index=True)
    repo = Column(String)
    branch = Column(String)
    status = Column(String)
    duration = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Failure(Base):
    __tablename__ = "failures"
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey("builds.id"))
    test_name = Column(String)
    error_message = Column(String)
    category = Column(String)
    build = relationship("Build", back_populates="failures")

Build.failures = relationship("Failure", back_populates="build")