from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(25), index=True)
    last_name = db.Column(db.String(25), index=True)

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)
