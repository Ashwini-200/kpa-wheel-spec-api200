from fastapi import FastAPI, HTTPException, Path, Depends
from sqlalchemy.orm import Session
import crud, models
from schemas import WheelSpecCreate, WheelSpec
from database import SessionLocal, engine, Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="KPA Wheel Specification API", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/wheel-specification", response_model=WheelSpec, status_code=201)
def create_wheel_spec(spec: WheelSpecCreate, db: Session = Depends(get_db)):
    return crud.create_wheel_spec(db, spec)

@app.get("/wheel-specification/{id}", response_model=WheelSpec)
def read_wheel_spec(id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    spec = crud.get_wheel_spec(db, id)
    if not spec:
        raise HTTPException(status_code=404, detail="Wheel specification not found")
    return spec
