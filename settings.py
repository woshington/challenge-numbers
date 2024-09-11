from decouple import config

PRECISION_FLOAT = config("PRECISION_FLOAT", cast=int, default=2)