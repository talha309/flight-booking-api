from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    is_admin: bool = False

class UserOut(BaseModel):
    id: int
    email: str
    is_admin: bool
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class FlightCreate(BaseModel):
    origin: str
    destination: str
    date: str
    time: str
    total_seats: int

class FlightOut(BaseModel):
    id: int
    origin: str
    destination: str
    date: str
    time: str
    total_seats: int
    available_seats: int
    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    flight_id: int
    seats_booked: int

class BookingOut(BaseModel):
    id: int
    user_id: int
    flight_id: int
    seats_booked: int
    class Config:
        orm_mode = True