import os
import sys
from dotenv import load_dotenv


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config():
    load_dotenv()

    config = {}

    missing = []

    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        config[var] = value

    return config, missing


def display_config(config):
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config.get("MATRIX_MODE", "unknown")
    print(f"Mode: {mode}")

    db = config.get("DATABASE_URL")
    if db:
        if "localhost" in db or "127.0.0.1" in db:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")
    else:
        print("Database: Not configured")

    api = config.get("API_KEY")
    if api:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config.get('LOG_LEVEL', 'UNKNOWN')}")

    zion = config.get("ZION_ENDPOINT")
    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check(config, missing):
    print("\nEnvironment security check:")

    if missing:
        print(f"[WARNING] Missing variables: {', '.join(missing)}")
    else:
        print("[OK] All required variables present")

    if any(v is None for v in config.values()):
        print("[WARNING] Some configuration values are not set")
    else:
        print("[OK] No hardcoded secrets detected")


    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found")


    if "MATRIX_MODE" in os.environ:
        print("[OK] Environment overrides available")
    else:
        print("[INFO] No runtime overrides detected")


def main():
    config, missing = load_config()

    if missing:
        print("WARNING: Missing configuration variables!")
        print("You should define them via environment variables or .env file.\n")

    display_config(config)
    security_check(config, missing)


if __name__ == "__main__":
    main()