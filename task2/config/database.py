from sqlalchemy.orm import as_declarative, Mapped, mapped_column


@as_declarative()
class BaseModel:
    id: Mapped[int] = mapped_column(primary_key=True)