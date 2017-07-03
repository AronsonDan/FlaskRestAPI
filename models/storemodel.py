from db import db


class StoreModel(db.Model):
    # state the table name
    __tablename__ = 'stores'

    # create table columns and define its attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # define the relationships between objects within the DB
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'name': self.name,
            'items': [item.json() for item in self.items.all()]
        }

    @classmethod
    def find_by_name(cls, name):
        # select * from items where name = name(function argument) limit 1
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        return self.json()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        return self.json()
