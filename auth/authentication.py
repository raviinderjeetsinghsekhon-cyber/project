import hashlib
from utils.db_handler import get_connection

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_admin() -> bool:
    print("\n--- Admin Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    hashed_pwd = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, hashed_pwd))
    user = cursor.fetchone()
    conn.close()

    if user and user[0] == 'admin':
        print("\nLogin successful! Welcome Admin.")
        return True
    else:
        print("\nInvalid admin credentials!")
        return False