from fastapi import APIRouter
from typing import List
from starlette.status import *
from db import database,tbl_provinsi, tbl_regency, tbl_district, tbl_village
from starlette.status import *
from sqlalchemy import asc

from .model_wilayah import ProvincesBase, RegenciesBase, DistrictsBase, VillagesBase

router = APIRouter()

@router.get("/getAllProvinces", response_model=List[ProvincesBase])
async def getAllProvinces():
    query = tbl_provinsi.select().order_by(asc(tbl_provinsi.c.name))
    return await database.fetch_all(query=query)

@router.get("/getRegencies/{idProvinsi}", response_model=List[RegenciesBase])
async def getRegencies(idProvinsi:str):
    query = tbl_regency.select().where(idProvinsi == tbl_regency.c.province_id).order_by(asc(tbl_regency.c.name))
    return await database.fetch_all(query=query)

@router.get("/getDistricts/{idRegency}", response_model=List[DistrictsBase])
async def getDistricts(idRegency:str):
    query = tbl_district.select().where(idRegency == tbl_district.c.regency_id).order_by(asc(tbl_district.c.name))
    return await database.fetch_all(query=query)

@router.get("/getVillages/{idDistrict}", response_model=List[VillagesBase])
async def getVillages(idDistrict:str):
    query = tbl_village.select().where(idDistrict == tbl_village.c.district_id).order_by(asc(tbl_village.c.name))
    return await database.fetch_all(query=query)