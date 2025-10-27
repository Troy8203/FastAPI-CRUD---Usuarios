import psycopg2
from fastapi import FastAPI, HTTPException
from psycopg2.extras import RealDictCursor

# Type Library
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="base-project",
        user="postgres",
        password="postgres"
    )

# Modelo para recibir JSON
class User(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[date] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None

# -------------------- GET TODOS LOS USUARIOS --------------------
@app.get("/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM usuarios ORDER BY id ASC")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

# -------------------- GET USUARIO POR ID --------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# -------------------- CREAR USUARIO --------------------
@app.post("/users")
def create_user(user: User):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
    """, (user.nombre, user.apellido, user.fecha_nacimiento, user.telefono, user.direccion))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Usuario creado exitosamente", "id": new_id}

# -------------------- ACTUALIZAR USUARIO --------------------
@app.patch("/users/{user_id}")
def update_user(user_id: int, user: User):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE usuarios
        SET nombre=%s, apellido=%s, fecha_nacimiento=%s, telefono=%s, direccion=%s
        WHERE id=%s
    """, (user.nombre, user.apellido, user.fecha_nacimiento, user.telefono, user.direccion, user_id))
    if cur.rowcount == 0:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Usuario actualizado exitosamente"}

# -------------------- ELIMINAR USUARIO --------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
    if cur.rowcount == 0:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Usuario eliminado exitosamente"}
