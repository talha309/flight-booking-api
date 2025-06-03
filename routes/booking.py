from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Booking, Flight, User
from schemas import BookingCreate, BookingOut
from database import get_db
from auth import get_current_user

router = APIRouter(prefix="/booking", tags=["Booking"])

@router.post("/", response_model=BookingOut)
def book_flight(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    flight = db.query(Flight).filter(Flight.id == booking.flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    if flight.available_seats < booking.seats_booked:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    flight.available_seats -= booking.seats_booked
    db.add(flight)

    new_booking = Booking(
        user_id=current_user.id,
        flight_id=booking.flight_id,
        seats_booked=booking.seats_booked
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@router.get("/my", response_model=list[BookingOut])
def my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Booking).filter(Booking.user_id == current_user.id).all()

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0fQ.xGS-R92CaI0Tnt0gN1v8Rk94FHnKDKmQlekr0KB4M_U"