"""
# Telegram AI Bot с интеграцией Bitrix24

## Описание
Этот бот выполняет анкетирование пользователей, ведет AI-диалог с GPT-4 и интегрируется с CRM Bitrix24.

## Установка
1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/your-repo/telegram-bot.git
   cd telegram-bot
   ```

2. Создайте файл `.env`:
   ```sh
   BOT_TOKEN=your_telegram_bot_token
   DB_URL=postgresql://user:password@db:5432/telegram_bot
   BITRIX_WEBHOOK=your_bitrix24_webhook
   OPENAI_API_KEY=your_openai_api_key
   ```

3. Запустите проект:
   ```sh
   docker-compose up --build -d
   ```

## Используемые технологии
- Python, Aiogram (Telegram Bot API)
- PostgreSQL (База данных)
- OpenAI API (GPT-4)
- Bitrix24 REST API (CRM-интеграция)
- Docker, Docker Compose (Деплой)

## Лицензия
MIT License.
"""
