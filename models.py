from sqlmodel import Field , SQLModel

class GPUGamingSurvey(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    Brand: str
    ModelName: str
    VramGB: int
    DollarPrice: int
    FavoriteGenre: str
    HoursPlayed: int
    PrimaryConsole: str
    MonitorResolution: str
    MouseType: str
    KeyboardType: str

