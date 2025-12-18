from sqlalchemy import create_engine
import os

def get_engine():
    """
    Create and return a SQLAlchemy engine for Neon PostgreSQL database.
    Uses environment variables or defaults for connection.
    """

    user = os.getenv("POSTGRES_USER", "neondb_owner")
    password = os.getenv("POSTGRES_PASSWORD", "contra_neon")
    host = os.getenv("POSTGRES_HOST", "host_neon")
    port = os.getenv("POSTGRES_PORT", "5432")
    database = os.getenv("POSTGRES_DB", "neondb")

    # IMPORTANT: Neon requires SSL mode
    connection_string = (
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
        f"?sslmode=require"
    )

    engine = create_engine(connection_string)
    return engine
