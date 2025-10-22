from flask import Flask
from app.config import Config

app = Flask(__name__) # Uygulama nesnesi oluşturuluyor
app.config.from_object(Config) # Yapılandırma ayarları yükleniyor

from app import routes # Uygulama URL yönlendirmeleri import ediliyor

