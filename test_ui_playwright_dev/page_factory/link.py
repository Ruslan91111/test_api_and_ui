"""Методы для работы со ссылками."""
from .component import Component


class Link(Component):
    @property
    def type_of(self) -> str:
        return 'link'

