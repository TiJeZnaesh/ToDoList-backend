#Используем официальный python образ
from python:3.11-slim

#устанавливаем рабочую директорию
WORKDIR /app

#копируем файл зависимостей
COPY requirements.txt .

#устанавливаем зависимость
RUN pip install -r requirements.txt

#копируем весь проект
COPY . .

#открываем порт
EXPOSE 8000

#запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
