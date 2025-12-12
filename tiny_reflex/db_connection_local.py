from sqlalchemy import create_engine
import os

def get_engine():
    """
    Create and return a SQLAlchemy engine for Neon PostgreSQL database.
    Uses environment variables or defaults for connection.
    """

    user = os.getenv("POSTGRES_USER", "myuser")
    password = os.getenv("POSTGRES_PASSWORD", "mypassword")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    database = os.getenv("POSTGRES_DB", "ecommerce_proyecto")

    # IMPORTANT: Neon requires SSL mode
    connection_string = (
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)
    return engine
