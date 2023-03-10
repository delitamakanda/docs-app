import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logging.info("Initializing the database...")
    init()
    logging.info("Database initialized.")


if __name__ == "__main__":
    main()
