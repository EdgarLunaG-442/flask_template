import datetime

from db import BaseModelMixin, db


class BlackList(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    blocked_reason = db.Column(db.String(200), nullable=True)
    ip = db.Column(db.String(200))
    create_date = db.Column(db.String(300), default=f'{datetime.datetime.utcnow()}')
    __mapper_args__ = {
        'confirm_deleted_rows': False
    }
