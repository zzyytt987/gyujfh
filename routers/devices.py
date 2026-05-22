from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from models import Device
from schemas import DeviceCreate, DeviceResponse
from auth import get_current_user
from models import User

router = APIRouter(prefix="/api/devices", tags=["devices"])


@router.get("", response_model=list[DeviceResponse])
def list_devices(
    category_id: int | None = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    q = db.query(Device)
    if category_id is not None:
        q = q.filter(Device.category_id == category_id)
    return q.all()


@router.get("/{device_id}", response_model=DeviceResponse)
def get_device(
    device_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dev = db.query(Device).filter(Device.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="设备不存在")
    return dev


@router.post("", response_model=DeviceResponse, status_code=201)
def create_device(
    body: DeviceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dev = Device(**body.model_dump())
    db.add(dev)
    db.commit()
    db.refresh(dev)
    return dev


@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(
    device_id: int,
    body: DeviceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dev = db.query(Device).filter(Device.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="设备不存在")
    for key, val in body.model_dump().items():
        setattr(dev, key, val)
    db.commit()
    db.refresh(dev)
    return dev


@router.delete("/{device_id}", status_code=204)
def delete_device(
    device_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    dev = db.query(Device).filter(Device.id == device_id).first()
    if not dev:
        raise HTTPException(status_code=404, detail="设备不存在")
    db.delete(dev)
    db.commit()
    return None
