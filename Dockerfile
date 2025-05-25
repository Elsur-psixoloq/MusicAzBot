# Python 3.10 imajı kullanılıyor
FROM python:3.10-slim

# Uygulama klasörünü oluştur
WORKDIR /app

# Gereken dosyaları kopyala
COPY . /app

# Gereken Python kütüphanelerini kur
RUN pip install --no-cache-dir -r requirements.txt

# Botu başlat
CMD ["python3", "-m", "MusicAzBot"]
