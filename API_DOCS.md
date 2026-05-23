# 企业移动办公 API 接口文档

**Base URL:** `http://<服务器IP>:8000`

**认证方式:** Bearer Token（除登录外所有接口需在 Header 中携带）

---

## 1. 认证

### 1.1 登录

```
POST /api/auth/login
```

**请求体：**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**成功响应 (200)：**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

**错误响应 (401)：**
```json
{ "detail": "用户名或密码错误" }
```

> **说明：** 登录成功后，后续所有请求需在 Header 中携带 `Authorization: Bearer {access_token}`。

---

## 2. 员工管理

### 2.1 获取员工列表

```
GET /api/employees
```

**请求头：** `Authorization: Bearer <token>`

**成功响应 (200)：**
```json
[
  {
    "id": 1,
    "name": "张伟",
    "age": 32,
    "email": "zhang.wei@corp.com",
    "department": "研发部"
  }
]
```

### 2.2 获取单个员工

```
GET /api/employees/{id}
```

**请求头：** `Authorization: Bearer <token>`

**成功响应 (200)：**
```json
{
  "id": 1,
  "name": "张伟",
  "age": 32,
  "email": "zhang.wei@corp.com",
  "department": "研发部"
}
```

**错误响应 (404)：**
```json
{ "detail": "员工不存在" }
```

### 2.3 新增员工

```
POST /api/employees
```

**请求头：** `Authorization: Bearer <token>`

**请求体：**
```json
{
  "name": "新员工",
  "age": 28,
  "email": "new@corp.com",
  "department": "研发部"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 员工姓名 |
| age | integer | 是 | 年龄 |
| email | string | 是 | 邮箱地址 |
| department | string | 是 | 所属部门 |

**成功响应 (201)：**
```json
{
  "id": 7,
  "name": "新员工",
  "age": 28,
  "email": "new@corp.com",
  "department": "研发部"
}
```

### 2.4 更新员工

```
PUT /api/employees/{id}
```

**请求头：** `Authorization: Bearer <token>`

**请求体：** 同新增，所有字段必填

**成功响应 (200)：** 返回更新后的员工对象

**错误响应 (404)：**
```json
{ "detail": "员工不存在" }
```

### 2.5 删除员工

```
DELETE /api/employees/{id}
```

**请求头：** `Authorization: Bearer <token>`

**成功响应 (204)：** 无返回体

---

## 3. 设备分类

### 3.1 获取分类列表

```
GET /api/categories
```

**请求头：** `Authorization: Bearer <token>`

**成功响应 (200)：**
```json
[
  {
    "id": 1,
    "name": "笔记本电脑",
    "description": "便携式计算设备"
  }
]
```

### 3.2 获取单个分类

```
GET /api/categories/{id}
```

**请求头：** `Authorization: Bearer <token>`

### 3.3 新增分类

```
POST /api/categories
```

**请求头：** `Authorization: Bearer <token>`

**请求体：**
```json
{
  "name": "新分类",
  "description": "分类描述信息"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 分类名称 |
| description | string | 否 | 分类描述，默认为空 |

**成功响应 (201)：** 返回创建的分类对象

### 3.4 更新分类

```
PUT /api/categories/{id}
```

**请求头：** `Authorization: Bearer <token>`

**请求体：** 同新增

### 3.5 删除分类

```
DELETE /api/categories/{id}
```

**请求头：** `Authorization: Bearer <token>`

**成功响应 (204)：** 无返回体

---

## 4. 设备管理

### 4.1 获取设备列表

```
GET /api/devices
GET /api/devices?category_id={分类ID}
```

**请求头：** `Authorization: Bearer <token>`

**查询参数：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| category_id | integer | 否 | 按分类筛选设备 |

**成功响应 (200)：**
```json
[
  {
    "id": 1,
    "name": "MacBook Pro 14",
    "model": "MBP2023",
    "category_id": 1,
    "status": "active"
  }
]
```

| 字段 | 说明 |
|------|------|
| status | `active` 正常 / `inactive` 停用 / `maintenance` 维护中 |

### 4.2 获取单个设备

```
GET /api/devices/{id}
```

**请求头：** `Authorization: Bearer <token>`

### 4.3 新增设备

```
POST /api/devices
```

**请求头：** `Authorization: Bearer <token>`

**请求体：**
```json
{
  "name": "新设备",
  "model": "型号",
  "category_id": 1,
  "status": "active"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 设备名称 |
| model | string | 是 | 设备型号 |
| category_id | integer | 是 | 所属分类 ID |
| status | string | 否 | 状态，默认 `active` |

**成功响应 (201)：** 返回创建的设备对象

### 4.4 更新设备

```
PUT /api/devices/{id}
```

**请求头：** `Authorization: Bearer <token>`

**请求体：** 同新增

### 4.5 删除设备

```
DELETE /api/devices/{id}
```

**请求头：** `Authorization: Bearer <token>`

**成功响应 (204)：** 无返回体

---

## 通用错误码

| 状态码 | 说明 |
|--------|------|
| 200 | 成功 |
| 201 | 创建成功 |
| 204 | 删除成功（无返回体） |
| 401 | token 无效或已过期 |
| 403 | 未携带 Authorization 请求头 |
| 404 | 资源不存在 |
| 422 | 请求参数校验失败 |

---

## 认证说明

所有需要认证的接口必须在请求头中携带：

```
Authorization: Bearer <access_token>
```

Token 通过 `/api/auth/login` 获取，有效期 24 小时。Token 过期后需重新登录。

---

## 测试数据

系统首次启动自动生成以下测试数据：

| 类型 | 数据 |
|------|------|
| 用户 | admin / admin123 |
| 员工 | 张伟、李娜、王芳、刘洋、陈静 |
| 分类 | 笔记本电脑、台式机、网络设备、外围设备 |
| 设备 | MacBook Pro 14、ThinkPad X1 Carbon、Dell OptiPlex 7090 等 6 台 |
