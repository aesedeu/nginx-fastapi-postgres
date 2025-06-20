from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from sqlalchemy.exc import IntegrityError

import models
import schemas
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user exists with the same email
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail=f"User with email {user.email} already exists"
        )
    
    # Check if username is taken
    existing_username = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_username:
        raise HTTPException(
            status_code=400,
            detail=f"Username {user.username} is already taken"
        )
    
    # Create new user
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Database error while creating user. Please try again."
        )

@app.post("/purchases/", response_model=schemas.Purchase)
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = models.Purchase(
        user_id=purchase.user_id,
        datetime=datetime.now(),
        sku_name=purchase.sku_name,
        price=purchase.price,
        quantity=purchase.quantity
    )
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

@app.get("/users/{user_id}/purchases/", response_model=List[schemas.Purchase])
def get_user_purchases(user_id: int, db: Session = Depends(get_db)):
    purchases = db.query(models.Purchase)\
        .filter(models.Purchase.user_id == user_id)\
        .order_by(models.Purchase.datetime.desc())\
        .limit(10)\
        .all()
    return purchases 