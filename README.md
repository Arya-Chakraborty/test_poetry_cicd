# AptWise Backend API

This project is a FastAPI backend for the AptWise application with authentication and Cassandra DB integration.

## Features

- FastAPI for high-performance REST API
- JWT-based authentication with cookie storage
- User registration, login, and account management
- Apache Cassandra integration for persistent data storage

## Prerequisites

- Python 3.11 or higher
- Poetry for dependency management
- Apache Cassandra (local installation or Docker)

## Getting Started with Cassandra

### Option 1: Using Docker

```bash
# Pull the Cassandra image
docker pull cassandra:latest

# Run the Cassandra container
docker run --name aptwisedb-cassandra -p 9042:9042 -d cassandra:latest

# Check the container status
docker ps
```

### Option 2: Local Installation

Follow the installation guide for your operating system from the [Apache Cassandra website](https://cassandra.apache.org/_/download.html).

## Environment Variables

Set the following environment variables or configure them in your deployment:

- `SECRET_KEY`: JWT secret key
- `CASSANDRA_HOST`: Cassandra host (default: 127.0.0.1)
- `CASSANDRA_PORT`: Cassandra port (default: 9042)
- `CASSANDRA_KEYSPACE`: Cassandra keyspace name (default: aptwisedb)
- `CASSANDRA_USERNAME`: Cassandra username (default: cassandra)
- `CASSANDRA_PASSWORD`: Cassandra password (default: cassandra)

## Installation and Setup

```bash
# Clone the repository
git clone https://github.com/your-username/aptwisedb.git
cd aptwisedb

# Install dependencies with poetry
poetry install

# Run the FastAPI server
poetry run python -m src.test_poetry_cicd.main
```

The API will be available at http://localhost:8000.

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc