from dataclasses import dataclass, field
from typing import Any


@dataclass
class Product:
    title: str
    reference: str = field(repr=False)
    description: str = field(repr=False)
    images_url: list[str] = field(default_factory=list)
    rrp: float = field(repr=False)
    price: float = field(repr=False) 
    currency: str = field(repr=False)
    url: str
    brand: str = field(repr=False)
    origin: str = field(repr=False)
    category: str = field(repr=False)
    composition: str = field(repr=False)
    color: str = field(repr=False)
    meta: Any = field(repr=False)
    gender: bool = field(repr=False)
