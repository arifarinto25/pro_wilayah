from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table)
from databases import Database

DATABASE_URL='mysql+mysqlconnector://root:admin@localhost:3306/wilayah'

# SQLAlchemy
metadata = MetaData()

tbl_provinsi = Table(
	'provinces',
	metadata,
	Column('id', String, unique=True, primary_key = True), 
	Column('name', String, unique=True)
)

tbl_regency = Table(
	'regencies',
	metadata,
	Column('id', String, unique=True, primary_key = True), 
	Column('province_id', String),
	Column('name', String)
)

tbl_district = Table(
	'districts',
	metadata,
	Column('id', String, unique=True, primary_key = True), 
	Column('regency_id', String),
	Column('name', String)
)

tbl_village = Table(
	'villages',
	metadata,
	Column('id', String, unique=True, primary_key = True), 
	Column('district_id', String),
	Column('name', String)
)

# databases query builder
database = Database(DATABASE_URL)
