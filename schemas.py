from pydantic import BaseModel

class WheelSpecBase(BaseModel):
    tread_diameter: float
    condemning_dia: float
    last_shop_issue_size: float
    wheel_gauge: float
    variation_same_axle: float

class WheelSpecCreate(WheelSpecBase):
    pass

class WheelSpec(WheelSpecBase):
    id: int

    class Config:
        orm_mode = True
