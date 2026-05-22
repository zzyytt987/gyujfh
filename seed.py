from database import SessionLocal, engine, Base
from models import User, Employee, Category, Device
from auth import hash_password


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(User).first():
        db.close()
        return

    db.add(User(username="admin", hashed_password=hash_password("admin123")))

    db.add_all([
        Employee(name="张伟", age=32, email="zhang.wei@corp.com", department="研发部"),
        Employee(name="李娜", age=28, email="li.na@corp.com", department="市场部"),
        Employee(name="王芳", age=35, email="wang.fang@corp.com", department="人力资源"),
        Employee(name="刘洋", age=41, email="liu.yang@corp.com", department="财务部"),
        Employee(name="陈静", age=26, email="chen.jing@corp.com", department="研发部"),
    ])

    db.add_all([
        Category(name="笔记本电脑", description="便携式计算设备"),
        Category(name="台式机", description="固定工作站"),
        Category(name="网络设备", description="交换机、路由器等"),
        Category(name="外围设备", description="显示器、键盘、鼠标"),
    ])

    db.flush()

    db.add_all([
        Device(name="MacBook Pro 14", model="MBP2023", category_id=1, status="active"),
        Device(name="ThinkPad X1 Carbon", model="X1C-Gen11", category_id=1, status="active"),
        Device(name="Dell OptiPlex 7090", model="OPX7090", category_id=2, status="active"),
        Device(name="Cisco Catalyst 2960", model="WS-C2960", category_id=3, status="maintenance"),
        Device(name="Dell U2722D", model="U2722D", category_id=4, status="active"),
        Device(name="HP EliteBook 840", model="EB840G9", category_id=1, status="inactive"),
    ])

    db.commit()
    db.close()
