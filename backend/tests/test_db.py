import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import Build

# Create a test DB (in-memory SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

def test_insert_build(db):
    build = Build(commit_hash="abc123", status="success", logs="Build OK")
    db.add(build)
    db.commit()
    db.refresh(build)
    assert build.id == 1
    assert build.status == "success"