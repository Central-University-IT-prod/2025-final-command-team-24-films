from fastapi import APIRouter, HTTPException, status, Header
from models.schemas import LogIn, Token
from adapters.db_source import DatabaseAdapter
import os
from dotenv import load_dotenv
import bcrypt
router = APIRouter()
load_dotenv()

@router.post("/truncate", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def truncate_all_tables(admin_key: str = Header(None)):
    adapter = DatabaseAdapter()
    if admin_key != os.getenv("ADMIN_KEY"):
        raise HTTPException(status_code=403, detail="Correct admin key required")
    adapter.connect()
    
    for i in ['collections','users','collections','films','films_to_users','friends']:
        adapter.truncate_table(i)

    hash_password = bcrypt.hashpw(os.getenv("ADMIN_PASSWORD").encode('utf-8'), bcrypt.gensalt(rounds=7))
    hash_password = str(hash_password)[2:-1]
    try:
        adapter.insert("users", {"email": "admin@example.com", "password": hash_password, "login": "admin", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwiZXhwIjoxNzQzNjU5MzY1fQ.CtFHqos2OC4jowb6jRXqLvGwGwzikzSbxc31U-fMgws"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "friend@example.com", "password": hash_password, "login": "friend", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZEBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.shydgm2Kw_NaceNAQWVbC9Bwz_FeS957ixAKE6FCUMQ"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "admin2@example.com", "password": hash_password, "login": "admin2", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluMkBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.ZPng-BqFgUFk_Jaop6qP-4l7jy10n_rGQKNLbeRCLb0"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "friend2@example.com", "password": hash_password, "login": "friend2", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDJAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.QXLCV39NpQ89TjsjvFQw6N6pbUOLkLteI-3ALcacDQA"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "admin3@example.com", "password": hash_password, "login": "admin3", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluM0BleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.776g4MKH-qiT6LyIMC7LMWelVRdSu4MAKS4d3lm8jy8"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "friend3@example.com", "password": hash_password, "login": "friend3", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDNAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.w7ZprHBAl3CxiVcJsQtq-Bfu3qjRx6T_HtT1OMvJH4Q"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "admin4@example.com", "password": hash_password, "login": "admin4", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluNEBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.SoHIUw64kqe_CDpEJxUKX-NWnp_KsNPAY0GtrCiXMjM"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "friend4@example.com", "password": hash_password, "login": "friend4", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDRAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.G3EX135wvaZTOqeQued4-Q6aRmVxj9Cyadd6ZgsOVM4"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "admin5@example.com", "password": hash_password, "login": "admin5", "token": "REDACTED.eyJlbWFpbCI6ImFkbWluNUBleGFtcGxlLmNvbSIsImV4cCI6MTc0MzY1OTM2NX0.oEO2QZZNVh2nKAkL7Jh2ocMKXr3FQzy6OFse89miviA"})
    except: adapter.connection.rollback()
    try:
        adapter.insert("users", {"email": "friend5@example.com", "password": hash_password, "login": "friend5", "token": "REDACTED.eyJlbWFpbCI6ImZyaWVuZDVAZXhhbXBsZS5jb20iLCJleHAiOjE3NDM2NTkzNjV9.joLVc_65CcRy-bIM6D_JvsctuQKcPTm8PNgzGslSotc"})
    except: adapter.connection.rollback()
