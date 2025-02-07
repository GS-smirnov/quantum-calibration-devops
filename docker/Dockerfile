# Использование базового образа Python 3.10 (или актуальной версии)
FROM python:3.10-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y build-essential

# Копирование файла requirements.txt и установка зависимостей Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование исходного кода
COPY . .

# Команда для запуска приложения (измените под нужный скрипт)
CMD ["python", "src/main.py"]
