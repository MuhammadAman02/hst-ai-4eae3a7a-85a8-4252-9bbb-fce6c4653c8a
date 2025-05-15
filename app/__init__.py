from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Import and include routers
from .api import routes as api_routes
from .frontend import routes as frontend_routes

app.include_router(api_routes.router, prefix="/api", tags=["api"])
app.include_router(frontend_routes.router, tags=["frontend"])