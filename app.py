"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake
from project_secrets import API_SECRET_KEY

app = Flask(__name__)

app.config['SECRET_KEY'] = API_SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


@app.route('/api/cupcakes')
def list_cupcakes():
    """ Get data about all cupcakes.

    Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}.

    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Get data about a single cupcake.

        Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from
        the body of the request.

        Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
    """

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

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Update a cupcake with the id passed in the URL and flavor, size,
    rating and image data from the body of the request.

    Respond with JSON of the newly-updated cupcake, like this: {cupcake:
    {id, flavor, size, rating, image}}.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    cupcake.flavor = flavor
    cupcake.size = size
    cupcake.rating = rating
    cupcake.image = image

    db.session.commit()
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Delete cupcake with the id passed in the URL.
    Respond with JSON like {message: "Deleted"}.
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)

    return jsonify(message="Deleted")
