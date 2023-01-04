from fastapi import FastAPI
from sqlalchemy import create_engine,Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI(title="My API", version="1.0", openapi_url="/api/v1/openapi.json")

# Replace user, password, host, and database with your own values
engine = create_engine("postgresql://offer-order:AVNS_9EMeUYeydmTeQjqJRlw@db-postgresql-fra1-94014-do-user-1669452-0.b.db.ondigitalocean.com/offer-order-db")

from typing import Dict, List

from fastapi import FastAPI
from fastapi import models

app = FastAPI()
    
    
@app.post("/partners")
def create_product(product: Product):
    #Create a session to manage the connection to the database:
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(product)
    session.commit()
    return {"id": product.id}


@app.get("/partners/{id}")
def get_product(id: str):
    # Code to retrieve the product
    #return product
    
    return {"id": id}

