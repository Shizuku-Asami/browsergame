from typing import BinaryIO

from ninja import Schema

class TerrainIn(Schema):
    x: int
    y: int
    image: BinaryIO

class TerrainOut(Schema):
    id: int
    x: int
    y: int
    image: BinaryIO