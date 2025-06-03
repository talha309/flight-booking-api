from fastapi import FastAPI
from database import Base, engine
from routes import user, flight, booking

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(flight.router)
app.include_router(booking.router)

# poetry run alembic revision --autogenerate -m"add flight & booking table"