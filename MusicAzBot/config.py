import os


class Config:

   API_ID = int(os.getenv("API_ID", "19769686"))
   API_HASH = os.getenv("API_HASH", "515b64f5d2d955cdd6aa85a808fd4cb4")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7340381347:AAFfVgtVNSyFCX-XNJav0gDGbRdXUODDRXA")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "XezerMusicRobot")
   OWNER_NAME = os.environ.get("OWNER_NAME", "Lerrodu") 
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "LerroBlogs")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002529622504"))
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "LERRO")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dc9794139c12507f5eb1c.jpg")    
