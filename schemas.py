from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ─── Employee ────────────────────────────────────────────────────────────────────

class EmployeeBase(BaseModel):
    name: str
    age: int
    email: str
    department: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int

    model_config = {"from_attributes": True}


# ─── Category ────────────────────────────────────────────────────────────────────

class CategoryBase(BaseModel):
    name: str
    description: str = ""


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    model_config = {"from_attributes": True}


# ─── Device ──────────────────────────────────────────────────────────────────────

class DeviceBase(BaseModel):
    name: str
    model: str
    category_id: int
    status: str = "active"


class DeviceCreate(DeviceBase):
    pass


class DeviceResponse(DeviceBase):
    id: int

    model_config = {"from_attributes": True}
