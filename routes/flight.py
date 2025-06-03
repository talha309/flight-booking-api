from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Flight
from schemas import FlightCreate, FlightOut
from database import get_db

router = APIRouter(prefix="/flights", tags=["Flights"])

@router.post("/", response_model=FlightOut)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    new_flight = Flight(**flight.dict(), available_seats=flight.total_seats)
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight

@router.get("/", response_model=list[FlightOut])
def get_all_flights(db: Session = Depends(get_db)):
    return db.query(Flight).all()