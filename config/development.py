from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

print(BASE_DIR)
print(SQLALCHEMY_DATABASE_URI)
print(SQLALCHEMY_TRACK_MODIFICATIONS)
print(SECRET_KEY)