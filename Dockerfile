# Используем официальный образ Python в качестве базового образа
FROM python:3.12
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app
# Копируем файл requirements.txt внутрь контейнера
COPY requirements.txt ./
# Скопируйте файлы проекта
COPY . /app/
# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r requirements.txt

# Установить утилиту psql и зависимости для PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client






