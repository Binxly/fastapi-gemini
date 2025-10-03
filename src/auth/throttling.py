import time, os
from collections import defaultdict
from fastapi import HTTPException, status
from dotenv import load_dotenv

load_dotenv()

user_requests = defaultdict(list)

def apply_rate_limit(user_id: str):
    current_time = time.time()

    if user_id == "global_unauthenticated_user":
        rate_limit = int(os.getenv("GLOBAL_RATE_LIMIT"))
        time_window = int(os.getenv("GLOBAL_TIME_WINDOW_SECONDS"))
    else:
        rate_limit = int(os.getenv("AUTH_RATE_LIMIT"))
        time_window = int(os.getenv("AUTH_TIME_WINDOW_SECONDS"))

    # filter messages older than the time window
    user_requests[user_id] = [
        t for t in user_requests[user_id] if t > current_time - time_window
    ]

    # Without proper authentication, all users share a user_id
    if len(user_requests[user_id]) >= rate_limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please try again later.",
        )

    user_requests[user_id].append(current_time)
    return True