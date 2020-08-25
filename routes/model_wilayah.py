from pydantic import BaseModel

class ProvincesBase(BaseModel):
    id: str = None
    name: str = None

class RegenciesBase(BaseModel):
    id: str = None
    province_id: str = None
    name: str = None

class DistrictsBase(BaseModel):
    id: str = None
    regency_id: str = None
    name: str = None

class VillagesBase(BaseModel):
    id: str = None
    district_id: str = None
    name: str = None