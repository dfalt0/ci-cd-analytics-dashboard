from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# /builds → list all builds
@app.get("/builds")
def get_builds(db: Session = next(get_db())):
    return db.query(models.Build).all()

# /builds/{id} → return build + logs
@app.get("/builds/{build_id}")
def get_build(build_id: int, db: Session = next(get_db())):
    build = db.query(models.Build).filter(models.Build.id == build_id).first()
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    return build
