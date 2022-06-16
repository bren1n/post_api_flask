from app import ma
from user.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User