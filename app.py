

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

## setup database engine
engine = create_engine("sqlite:///hawaii.sqlite")

## reflect databse into class
Base = automap_base()
Base.prepare(engine, reflect=True)

## create variables for each class

Measurement = Base.classes.measurement
Station = Base.classes.station

## create a session link from Python to our database
session = Session(engine)


## create a new flask app instance ** always the same **
app = Flask(__name__)

## define the starting point (root)
@app.route('/')
def Welcome():
    return (
        '''
        Welcome to the Climat Analysis API!\n
        Available routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')
    

@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
    
