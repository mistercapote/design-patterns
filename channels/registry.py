from typing import Type
from channels.base import ChannelFactory
from channels.web import WebFactory
from channels.mobile import MobileFactory

# Questão 05

# Dicionário interno de fábricas registradas
_CHANNEL_REGISTRY: dict[str, Type[ChannelFactory]] = {}


def register_channel_factory(channel: str, factory_cls: Type[ChannelFactory]) -> None:
    """Registra uma nova fábrica associada a um identificador de canal."""
    _CHANNEL_REGISTRY[channel.upper()] = factory_cls


def get_channel_factory(channel: str) -> ChannelFactory:
    """Retorna uma instância da fábrica correspondente ou levanta erro claro."""
    channel_key = channel.upper()
    factory_cls = _CHANNEL_REGISTRY.get(channel_key)
    
    if factory_cls is None:
        raise ValueError(f"Canal desconhecido: '{channel}'. Canais disponiveis: {list(_CHANNEL_REGISTRY.keys())}")
        
    return factory_cls()


# Registro inicial exigido pelo enunciado
register_channel_factory("WEB", WebFactory)
register_channel_factory("MOBILE", MobileFactory)