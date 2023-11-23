from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class WinnerData(BaseModel):
    team1: str
    team2: str 