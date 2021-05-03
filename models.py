"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

DEFAULT_CUPCAKE_IMG = 'https://tinyurl.com/demo-cupcake'

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String(50),
                    nullable=False)               
    size = db.Column(db.String(50),
                    nullable=False)

    rating = db.Column(db.Integer,
                    nullable=False)
    image = db.Column(db.Text, 
                    nullable=False, 
                    default=DEFAULT_CUPCAKE_IMG)

    def serialize(self):
        """Serialize to dictionary."""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }

    def __repr__(self):
        """Show info about cupcake."""

        c = self
        return f"<Cupcake {c.id} {c.flavor} {c.size} {c.rating}>"