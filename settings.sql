-- settings.sql
CREATE DATABASE nostaldja;
CREATE USER NostaldjaUser WITH PASSWORD 'nostaldja';
GRANT ALL PRIVILEGES ON DATABASE nostaldja TO nostaldjauser;