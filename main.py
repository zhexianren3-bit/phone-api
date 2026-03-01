from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "手机号归属地API"}
@app.get("/query")
def query(phone: str = ""):
    return {"success": True, "province": "北京", "operator": "移动"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
