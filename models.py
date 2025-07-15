from sqlalchemy import Column, Integer, Float
from database import Base

class WheelSpec(Base):
    __tablename__ = "wheel_spec"
    id = Column(Integer, primary_key=True, index=True)
    tread_diameter = Column(Float, nullable=False)
    condemning_dia = Column(Float, nullable=False)
    last_shop_issue_size = Column(Float, nullable=False)
    wheel_gauge = Column(Float, nullable=False)
    variation_same_axle = Column(Float, nullable=False)
