from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.core.config import settings
from app.core.database import init_db
from app.api import auth, users, canvases, widgets, ai_services
from app.middleware.logging import log_requests
from app.middleware.rate_limiting import rate_limiter
import asyncio

# Initialize FastAPI app
app = FastAPI(
    title="Widget Canvas Builder API",
    description="API for widget canvas builder with AI integrations",
    version="1.0.0"
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]  # Configure appropriately for production
)

app.middleware("http")(log_requests)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(canvases.router)
app.include_router(widgets.router)
app.include_router(ai_services.router)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()

@app.get("/")
async def root():
    return {"message": "Widget Canvas Builder API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)