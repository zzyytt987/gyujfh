from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, employees, categories, devices
from seed import seed

app = FastAPI(title="企业移动办公 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(categories.router)
app.include_router(devices.router)


@app.on_event("startup")
def on_startup():
    seed()
