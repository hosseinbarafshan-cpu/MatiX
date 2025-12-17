from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Cabinet Unit Calculator")

class UnitInput(BaseModel):
    width: int
    height: int
    depth: int

@app.get("/")
def home():
    return {"status": "ok", "message": "Cabinet Unit Calculator is running"}

@app.post("/calculate")
def calculate(unit: UnitInput):
    panels = {
        "side_panels": [
            {"width": unit.depth, "height": unit.height},
            {"width": unit.depth, "height": unit.height}
        ],
        "top_panel": {"width": unit.width, "depth": unit.depth},
        "bottom_panel": {"width": unit.width, "depth": unit.depth},
        "back_panel": {"width": unit.width, "height": unit.height}
    }

    return {
        "input": unit,
        "cut_list": panels
    }
