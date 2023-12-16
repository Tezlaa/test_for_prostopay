from sqlalchemy.orm import mapped_column, Mapped

from config.database import BaseModel


class UsersModel(BaseModel):
    __tablename__ = 'users'
    
    username: Mapped[str] = mapped_column()