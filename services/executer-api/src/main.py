from fastapi import FastAPI, HTTPException
import subprocess
import uvicorn

app = FastAPI()


@app.post("/on")
async def turn_on():
    try:
        subprocess.run(["sudo uhubctl -l 2 -a on"], check=True, shell=True)
        return {"message": "Device is now ON"}
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Failed to turn device on")


@app.post("/off")
async def turn_off():
    try:
        subprocess.run(["sudo uhubctl -l 2 -a off"], check=True, shell=True)
        return {"message": "Device is now OFF"}
    except subprocess.CalledProcessError:
        raise HTTPException(
            status_code=500, detail="Failed to turn device off")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload=True)
