import logging
import time
from fastapi import Request, Response
from typing import Callable
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def log_requests(request: Request, call_next: Callable) -> Response:
    """Middleware to log all requests"""
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    # Log request
    logger.info(
        f"Request {request_id}: {request.method} {request.url} "
        f"from {request.client.host}"
    )
    
    # Process request
    response = await call_next(request)
    
    # Log response
    process_time = time.time() - start_time
    logger.info(
        f"Response {request_id}: {response.status_code} "
        f"in {process_time:.4f}s"
    )
    
    # Add request ID to response headers
    response.headers["X-Request-ID"] = request_id
    
    return response