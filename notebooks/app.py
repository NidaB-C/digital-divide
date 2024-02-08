# Import the dependencies.
import numpy as np
import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import desc

from flask import Flask, jsonify


engine = create_engine("sqlite:///database.sqlite")

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    session = Session(engine)
    execute_string = "select * from ActivityTypes"
    activity_types = engine.execute(execute_string).fetchall()
    session.close()

    activity_type_dict = []
    for row in activity_types:
        activity_type = {row[0]:row[1]}
        activity_type_dict.append(activity_type)
        
    return(jsonify(activity_type_dict))


if __name__ == '__main__':
    app.run(debug=True)
