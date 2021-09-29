# +++++++++++ DJANGO +++++++++++
# Aby użyć własnej aplikacji Django, użyj kodu w następujący sposób:
import  os
import  sys
path = '/home/wojtek92/collection_of_English_learning_materials'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collection_of_English_learning_materials.settings')

application = get_wsgi_application()

# from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(application)
