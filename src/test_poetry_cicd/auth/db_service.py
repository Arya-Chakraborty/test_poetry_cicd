"""
Database services for authentication.
"""
from typing import Optional, Dict, List, Any
from ..config import get_session

session = get_session()


def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Get user by email from the database."""
    if not session:
        raise RuntimeError("Database connection not available")

    query = "SELECT * FROM users WHERE email = %s"
    result = session.execute(query, [email])
    user = result.one()

    if not user:
        return None

    return {
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "linkedin_url": user.linkedin_url,
        "github_url": user.github_url
    }


def create_user(user_data: Dict[str, Any]) -> bool:
    """Create a new user in the database."""
    if not session:
        raise RuntimeError("Database connection not available")

    query = """
    INSERT INTO users (email, name, password, linkedin_url, github_url)
    VALUES (%s, %s, %s, %s, %s)
    """

    try:
        session.execute(
            query,
            [
                user_data["email"],
                user_data["name"],
                user_data["password"],
                user_data.get("linkedin_url", None),
                user_data.get("github_url", None)
            ]
        )
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        return False


def delete_user(email: str) -> bool:
    """Delete a user from the database."""
    if not session:
        raise RuntimeError("Database connection not available")

    query = "DELETE FROM users WHERE email = %s"

    try:
        session.execute(query, [email])
        return True
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False


def get_all_users() -> List[Dict[str, Any]]:
    """Get all users from the database."""
    if not session:
        raise RuntimeError("Database connection not available")

    query = "SELECT * FROM users"
    results = session.execute(query)

    users = []
    for user in results:
        users.append({
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "linkedin_url": user.linkedin_url,
            "github_url": user.github_url
        })

    return users
