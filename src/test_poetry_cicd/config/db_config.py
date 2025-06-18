"""
Database configuration for Cassandra DB.
"""
import os
from cassandra.cluster import Cluster

# Cassandra connection settings
CASSANDRA_HOST = os.getenv("CASSANDRA_HOST", "127.0.0.1")
CASSANDRA_PORT = int(os.getenv("CASSANDRA_PORT", "9042"))
CASSANDRA_KEYSPACE = os.getenv("CASSANDRA_KEYSPACE", "test_poetry_cicd")

# Initialize cluster connection without authentication (local setup)
cluster = Cluster(
    contact_points=[CASSANDRA_HOST],
    port=CASSANDRA_PORT
)

try:
    print(f"Attempting to connect to Cassandra \
          at {CASSANDRA_HOST}:{CASSANDRA_PORT}...")
    import traceback
    try:
        session = cluster.connect()
        print("Successfully connected to Cassandra cluster")
    except Exception as detailed_error:
        traceback.print_exc()
        raise detailed_error
except Exception as e:
    print(f"Error connecting to Cassandra: {e}")
    print(f"Connection details: Host={CASSANDRA_HOST}, Port={CASSANDRA_PORT}")
    print("ERROR: Cannot connect to Cassandra. \
          Application requires a database connection.")
    session = None

# Create keyspace if it doesn't exist
if session:
    try:
        print(f"Creating keyspace {CASSANDRA_KEYSPACE} if it doesn't exist...")
        session.execute(f"""
            CREATE KEYSPACE IF NOT EXISTS {CASSANDRA_KEYSPACE}
            WITH replication = {{'class': 'SimpleStrategy', \
                                'replication_factor': '1'}}
        """)
        print(f"Successfully created/verified keyspace: {CASSANDRA_KEYSPACE}")

        # Connect to our keyspace
        session.set_keyspace(CASSANDRA_KEYSPACE)

        # Create users table if it doesn't exist
        session.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                email text PRIMARY KEY,
                name text,
                password text,
                linkedin_url text,
                github_url text
            )
            """
        )
    except Exception as e:
        print(f"Error setting up keyspace: {e}")


def get_session():
    """Return the Cassandra session."""
    return session


def create_tables():
    """Create any necessary tables if they don't exist."""
    # Tables are created when the module is imported,
    # no need to do anything here
