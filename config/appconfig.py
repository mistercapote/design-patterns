# Questão 01

class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance.environment = "production"
            cls._instance.currency = "BRL"
            cls._instance.debug = False
        return cls._instance

