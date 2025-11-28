from fastapi import FastAPI
from typing import List

app = FastAPI()

# Temporary in-memory "database"
profiles = []

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/profiles")
def list_profiles():
    return profiles

@app.post("/api/profiles")
def create_profile(profile: dict):
    profile["id"] = len(profiles) + 1
    profiles.append(profile)
    return profile
