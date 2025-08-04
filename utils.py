# Simple file with utility files
from datetime import datetime, timedelta

def getDate():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getRefresh():
    return 60 - datetime.minute if datetime.minute != 0 else 0 
