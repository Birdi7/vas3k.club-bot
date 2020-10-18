import random
import socket
import time
from datetime import datetime, timedelta

CLUB_HOST, CLUB_PORT = "app", 8000

if __name__ == "__main__":
    started_at = datetime.utcnow()
    while datetime.utcnow() < started_at + timedelta(minutes=5):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((CLUB_HOST, CLUB_PORT))
                print("Club had started")
                break
        except socket.error:
            print("Waiting for club")
            time.sleep(0.5 + (random.randint(0, 100) / 1000))
