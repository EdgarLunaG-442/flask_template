from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import BlackList


class BlacklistSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BlackList
        include_relationships = True
        load_instance = True
        include_fk = True
