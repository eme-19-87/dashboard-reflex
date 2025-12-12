from sqlalchemy import create_engine
import os

def get_engine():
    """
    Create and return a SQLAlchemy engine for Neon PostgreSQL database.
    Uses environment variables or defaults for connection.
    """

    user = os.getenv("POSTGRES_USER", "neondb_owner")
    password = os.getenv("POSTGRES_PASSWORD", "npg_ZL5SKQRtp1OY")
    host = os.getenv("POSTGRES_HOST", "ep-polished-wave-adgxnoki-pooler.c-2.us-east-1.aws.neon.tech")
    port = os.getenv("POSTGRES_PORT", "5432")
    database = os.getenv("POSTGRES_DB", "neondb")

    # IMPORTANT: Neon requires SSL mode
    connection_string = (
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
        f"?sslmode=require"
    )

    engine = create_engine(connection_string)
    return engine
