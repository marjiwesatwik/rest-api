from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    items = db.relationship("ItemModel", back_populates="store", cascade="all, delete")
    tags = db.relationship("TagModel", back_populates="store", cascade="all, delete", lazy="dynamic")
    # lazy="dynamic" means that 'tags' will be a query that we can further refine before loading the items