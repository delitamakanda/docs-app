from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.base_class import Base

if TYPE_CHECKING:
    from db.post import Post  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)
    is_admin = Column(Boolean(), default=False)
    posts = relationship("Post", back_populates="owner")

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"