# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Hawaii = Base.classes.hawaii


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app1 = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app1.route("/")

def home():
    print("Server received request for 'Home' page...")
    return(
        f"Katrina's Hawaii Climate Data!<br/"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )


@app1.route("/api/v1.0/precipitation")

def precipitation():

    """Convert the query results from your precipitation analysis to a dictionary using date as the key and prcp as the value."""
    # Query aprecipitation data
    results = session.query(Hawaii.date, Hawaii.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of dates
    prcp_data = []

    for prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["percipitation"] = prcp
        prcp_data.append(prcp_dict)

    return jsonify(prcp_data)

@app1.route("/api/v1.0/stations")
def stations():

    """Return a list of stations"""
    # Query all stations
    results = session.query(Hawaii.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app1.route("/api/v1.0/tobs")
def tobs():
    """Return a list of tempature observations"""
    # Query all stations
    results = session.query(Hawaii.tobs).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)
