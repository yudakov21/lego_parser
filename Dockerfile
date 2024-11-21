FROM python:3.11.3

# Установим переменные окружения
ENV AM_I_IN_DOCKER 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установим рабочую директорию
WORKDIR /lego

# Обновление системы и установка необходимых пакетов
RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
       firefox-esr \
       xvfb \              
       libgtk-3-0 \        
       libdbus-glib-1-2 \  
       ca-certificates \
   && update-ca-certificates

# Копируем зависимости и устанавливаем их
COPY requirements.txt /lego/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем проект и настраиваем entrypoint
COPY ./entrypoint.sh .
COPY . .
RUN ["chmod", "+x", "entrypoint.sh"]

# Запуск контейнера
ENTRYPOINT ["/lego/entrypoint.sh"]
