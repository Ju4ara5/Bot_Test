"""
Подключение к PostgreSQL
"""
import asyncpg
import os

DB_URL = os.getenv("DB_URL")


async def init_db():
    return await asyncpg.create_pool(DB_URL)


async def save_user_data(user_id, name, phone, email, category):
    async with await init_db() as conn:
        await conn.execute(
            "INSERT INTO users (user_id, name, phone, email, category) VALUES ($1, $2, $3, $4, $5) ON CONFLICT (user_id) DO UPDATE SET name = $2, phone = $3, email = $4, category = $5",
            user_id, name, phone, email, category
        )
