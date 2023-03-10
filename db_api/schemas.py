from typing import Optional

from pydantic import BaseModel


class BaseMenu(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    dishes_count: Optional[int]
    submenus_count: Optional[int]

    class Config:
        orm_mode = True


class PatchMenu(BaseMenu):
    id: Optional[int]
    title: str
    description: str
    dishes_count: Optional[int]


class BaseSubmenu(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    dishes_count: Optional[int]

    class Config:
        orm_mode = True


class PatchSubmenu(BaseSubmenu):
    title: Optional[str]
    description: Optional[str]


class BaseDish(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    price: Optional[str]

    class Config:
        orm_mode = True


class UpgradeDish(BaseDish):
    title: str
    description: str
    price: float
