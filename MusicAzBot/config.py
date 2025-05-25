import os


class Config:

   API_ID = int(os.getenv("API_ID", "19769686"))
   API_HASH = os.getenv("API_HASH", "515b64f5d2d955cdd6aa85a808fd4cb4")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7342273596:AAFnVl_X1FYGgIpOTUVYuYRVPIGHVO_E7EE")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "NergizMusicBot")
   OWNER_NAME = os.environ.get("OWNER_NAME", "Elsur_psixoloq") 
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "Anonim_Sair")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-2422436777"))
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "ELSUR")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dc9794139c12507f5eb1c.jpg")    
