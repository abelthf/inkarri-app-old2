class BaseConfig:
    """Configuracion base del proyecto"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Configuracion de desarrollo"""
    pass

class TestingConfig(BaseConfig):
    """Configuracion de pruebas"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Configuracion de produccion"""
    pass