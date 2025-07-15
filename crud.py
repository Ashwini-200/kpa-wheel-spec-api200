from sqlalchemy.orm import Session
import models, schemas

def create_wheel_spec(db: Session, spec: schemas.WheelSpecCreate):
    db_spec = models.WheelSpec(**spec.dict())
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_wheel_spec(db: Session, id: int):
    return db.query(models.WheelSpec).filter(models.WheelSpec.id == id).first()
