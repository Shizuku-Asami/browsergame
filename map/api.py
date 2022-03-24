from ninja import NinjaAPI
from django.shortcuts import get_object_or_404

from .models import Terrain
from .schemas import TerrainIn, TerrainOut

api = NinjaAPI()


@api.post("/map", response=TerrainOut)
def create_terrain(request, payload: TerrainIn):
    terrain = Terrain.objects.create(**payload.dict())
    return terrain


@api.get("/map", response=TerrainOut)
def get_terrain_by_coordinates(request, x: int, y: int):
    terrain = get_object_or_404(Terrain, x=x, y=y)
    return terrain


@api.get("/map", response=TerrainOut)
def get_terrain_by_id(request, terrain_id: int):
    terrain = get_object_or_404(Terrain, id=terrain_id)
    return terrain


@api.put("/map", response=TerrainOut)
def update_terrain(request, terrain_id: int, payload: TerrainIn):
    terrain = get_object_or_404(Terrain, id=terrain_id)
    for attr, value in payload.dict().items():
        setattr(terrain, attr, value)
    terrain.save()
    return terrain


@api.delete("/map")
def delete_terrain(request, terrain_id: int):
    terrain = get_object_or_404(Terrain, id=terrain_id)
    terrain.delete()
    return {"success": True}
