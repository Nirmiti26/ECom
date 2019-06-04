import os

from django.conf import settings

UPLOAD_TO = os.path.join(settings.BASE_DIR, 'static/product_images')
