from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Product:
    title: str
    url: Optional[str]
    reference: str = field(repr=False)
    description: Optional[str] = field(repr=False)
    rrp: Optional[float] = field(repr=False)
    price: float = field(repr=False) 
    currency: str = field(repr=False)
    brand: Optional[str] = field(repr=False)
    category: Optional[str] = field(repr=False)
    composition: Optional[str] = field(repr=False)
    color: Optional[str] = field(repr=False)
    meta: Optional[list[dict[str,str]]] = field(default_factory=list)
    gender: Optional[bool] = field(repr=False)
    images_url: Optional[list[str]] = field(default_factory=list)
