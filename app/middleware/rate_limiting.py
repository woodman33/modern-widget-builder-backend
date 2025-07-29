from fastapi import Request, HTTPException, status
from typing import Dict, Optional
import time
import asyncio
from collections import defaultdict, deque
from app.core.config import settings

class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(deque)
        self.lock = asyncio.Lock()
    
    async def is_allowed(self, identifier: str, limit: int = None, window: int = None) -> bool:
        """Check if request is allowed based on rate limiting rules"""
        limit = limit or settings.rate_limit_requests
        window = window or settings.rate_limit_window
        
        async with self.lock:
            now = time.time()
            user_requests = self.requests[identifier]
            
            # Remove old requests outside the time window
            while user_requests and user_requests[0] <= now - window:
                user_requests.popleft()
            
            # Check if under limit
            if len(user_requests) < limit:
                user_requests.append(now)
                return True
            
            return False
    
    async def check_rate_limit(self, request: Request, identifier: str = None):
        """Middleware function to check rate limits"""
        if not identifier:
            identifier = request.client.host
        
        if not await self.is_allowed(identifier):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Please try again later."
            )

# Global rate limiter instance
rate_limiter = RateLimiter()