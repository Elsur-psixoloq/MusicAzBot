# Python 3.10 imajı kullanılıyor
FROM python:3.10-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["python3", "-m", "MusicAzBot"]
