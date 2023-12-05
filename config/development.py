import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = b'}\xbcz\xae\xa3g Nk\x1b\x8a\x05\xccl$\x13'

