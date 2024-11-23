from core.database import db_connection
from typing import Optional,Dict
from helper.password_hash import hash_password

def create_user(username: str, password: str) -> Optional[Dict[str,str]]:
    if not username or not password:
        raise ValueError("Username and password cannot be empty.")

    hashed_password = hash_password(password)
    query = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"

    try:
        with db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (username, hashed_password))
                connection.commit()
                return {"message":"success"} 
    except Exception as e:
        print(f"Error creating user: {e}")
        return {"message":"failure"}
