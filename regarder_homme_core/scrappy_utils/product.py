from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Product:
    title: str
    url: Optional[str]
    reference: str = field(repr=False)
    price: float = field(repr=False) 
    currency: str = field(repr=False)
    rrp: Optional[float] = field(repr=False, default_factory=None)
    description: Optional[str] = field(repr=False, default_factory=None)
    brand: Optional[str] = field(repr=False, default_factory=None)
    category: Optional[str] = field(repr=False, default_factory=None)
    composition: Optional[str] = field(repr=False, default_factory=None)
    color: Optional[str] = field(repr=False, default_factory=None)
    gender: Optional[bool] = field(repr=False, default_factory=None)
    meta: Optional[list[dict[str,str]]] = field(default_factory=list)
    images_url: Optional[list[str]] = field(default_factory=list)