# Import the dependencies.
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    print('Returning to homepage')
    return 'precipitation found at: "/api/v1.0/precipitation"'

def precipitation('/api/v1.0/precipitation'):
    print('Finding precipitation')
    return jsonify(dict(precip_df))

def station('/api/v1.0/stations'):
    print('Finding stations')
    return jsonify(most_active_stations)

def temps('/api/v1.0/tobs'):
    print('Finding temperature observations')
    return jsonify(dict(twelve_mon_temp))

def start('api/v1.0/<start>'):
    print ('Finding starting information')
    return jsonify(<start>)

def stop('api/v1.0/<start>/<end>'):
    print ('Finding starting information')
    return jsonify(<start><end>)