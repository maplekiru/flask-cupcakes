"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

@app.route('/api/cupcakes')
def list_cupcakes():
    """ Return a list of cupcakes """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes = serialized)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake_info(cupcake_id):
    """ Return information of cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake = serialized)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """ Create a cupcake and returns cupcake information """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    cupcake = Cupcake(
        flavor=flavor, 
        size=size, 
        rating=rating, 
        image=image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake = serialized), 201)