"""
Simple script to test Cassandra connection.
"""
import traceback
from cassandra.cluster import Cluster

def test_connection():
    try:
        # Try to connect to Cassandra
        print("Attempting to connect to Cassandra at 127.0.0.1:9042...")
        cluster = Cluster(['127.0.0.1'], port=9042)
        session = cluster.connect()
        
        # If we get here, connection was successful
        print("Successfully connected to Cassandra!")
        
        # Get cluster information
        rows = session.execute("SELECT cluster_name, release_version FROM system.local")
        for row in rows:
            print(f"Connected to cluster: {row.cluster_name} with release version: {row.release_version}")
        
        # Close the connection
        cluster.shutdown()
        return True
    except Exception as e:
        print(f"Error connecting to Cassandra: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_connection()
    if success:
        print("Cassandra connection test passed!")
    else:
        print("Cassandra connection test failed!")
