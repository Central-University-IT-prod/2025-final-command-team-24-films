from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi_server.auth import router as authorization_router
from fastapi_server.screenshots import router as screenshots_router
from fastapi_server.films import router as films_router
from fastapi_server.social import router as social_router
from fastapi_server.collections import  router as collection_router
from fastapi_server.service import router as service_router
from fastapi_server.ai import router as ai_router
from fastapi import FastAPI
from adapters.db_source import DatabaseAdapter
import os
import time
import bcrypt
load_dotenv()
'''def load_custom_openapi():
    with open("backend/openapi(1).json", "r") as file:
        return json.load(file)'''

app = FastAPI(docs_url="/api/docs",openapi_url="/api/openapi.json")
'''app.openapi_schema = app.openapi()
app.openapi_schema["security"] = [{"OAuth2PasswordBearer": []}]'''

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)
    
app.include_router(authorization_router, prefix="/api/auth", tags=["Auth"])
app.include_router(screenshots_router, prefix="/api/screenshots", tags=["Screenshots"])
app.include_router(films_router, prefix="/api/films", tags=["Films"])
app.include_router(collection_router, prefix="/api/collections", tags=["Collections"])
app.include_router(social_router, prefix="/api/social", tags=["Social"])
app.include_router(service_router, prefix="/api/service", tags=["Service"])
app.include_router(ai_router, prefix="/api/ai", tags=["AI"])


if __name__ == "__main__":
    host, port = os.getenv("FAST_API_HOST"), os.getenv("FAST_API_PORT")
    time.sleep(10)
    db = DatabaseAdapter()
    db.connect()
    db.initialize_tables()
    hash_password = bcrypt.hashpw(os.getenv("ADMIN_PASSWORD").encode('utf-8'), bcrypt.gensalt(rounds=7))
    hash_password = str(hash_password)[2:-1]
    try:
        db.insert("users", {"email": "admin@example.com", "password": hash_password, "login": "admin", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwiZXhwIjoxNzQzNjU5MzY1fQ.CtFHqos2OC4jowb6jRXqLvGwGwzikzSbxc31U-fMgws"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "friend@example.com", "password": hash_password, "login": "friend", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZEBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.shydgm2Kw_NaceNAQWVbC9Bwz_FeS957ixAKE6FCUMQ"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "admin2@example.com", "password": hash_password, "login": "admin2", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluMkBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.ZPng-BqFgUFk_Jaop6qP-4l7jy10n_rGQKNLbeRCLb0"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "friend2@example.com", "password": hash_password, "login": "friend2", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDJAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.QXLCV39NpQ89TjsjvFQw6N6pbUOLkLteI-3ALcacDQA"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "admin3@example.com", "password": hash_password, "login": "admin3", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluM0BleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.776g4MKH-qiT6LyIMC7LMWelVRdSu4MAKS4d3lm8jy8"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "friend3@example.com", "password": hash_password, "login": "friend3", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDNAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.w7ZprHBAl3CxiVcJsQtq-Bfu3qjRx6T_HtT1OMvJH4Q"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "admin4@example.com", "password": hash_password, "login": "admin4", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluNEBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.SoHIUw64kqe_CDpEJxUKX-NWnp_KsNPAY0GtrCiXMjM"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "friend4@example.com", "password": hash_password, "login": "friend4", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDRAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.G3EX135wvaZTOqeQued4-Q6aRmVxj9Cyadd6ZgsOVM4"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "admin5@example.com", "password": hash_password, "login": "admin5", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluNUBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.oEO2QZZNVh2nKAkL7Jh2ocMKXr3FQzy6OFse89miviA"})
    except: db.connection.rollback()
    try:
        db.insert("users", {"email": "friend5@example.com", "password": hash_password, "login": "friend5", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDVAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.joLVc_65CcRy-bIM6D_JvsctuQKcPTm8PNgzGslSotc"})
    except: db.connection.rollback()
    uvicorn.run(app, host=host, port=int(port))
    