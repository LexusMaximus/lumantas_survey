from sqlmodel import Session , select

from database import create_db_and_tables, engine
from models import GPUGamingSurvey



def main():
    create_db_and_tables()
    # what you want to do here

    
    survey1 = GPUGamingSurvey(Brand='NVIDIA', ModelName='RTX 4090', VramGB=24, DollarPrice=1000, FavoriteGenre='RPG', HoursPlayed=20, PrimaryConsole='PC', MonitorResolution='4K', MouseType='Wireless', KeyboardType='Mechanical')
    survey2 = GPUGamingSurvey(Brand='AMD', ModelName='RX 7900 XTX', VramGB=24, DollarPrice=799, FavoriteGenre='FPS', HoursPlayed=15, PrimaryConsole='PC', MonitorResolution='1440p', MouseType='Wired', KeyboardType='Membrane')
    survey3 = GPUGamingSurvey(Brand='Intel', ModelName='Arc A770', VramGB=16, DollarPrice=699, FavoriteGenre='MOBA', HoursPlayed=30, PrimaryConsole='PC', MonitorResolution='1080p', MouseType='Wired', KeyboardType='Mechanical')

    with Session(engine) as session:
        session.add(survey1)
        session.add(survey2)
        session.add(survey3)
        session.commit()


if __name__ == "__main__":
    main()