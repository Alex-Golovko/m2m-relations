import os
# from website.settings import BASE_DIR

SECRET_KEY = 'b0e@^m&tccz11$w59qov$lhn-97!(%wfn-gray-c*x)^a$wx=2'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}