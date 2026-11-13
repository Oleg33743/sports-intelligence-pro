from fastapi import FastAPI
app=FastAPI(title="SPORTS INTELLIGENCE PRO API")
SPORTS=[{"id":x,"name":n} for x,n in [("football","Футбол"),("hockey","Хоккей"),("cs2","CS2"),("dota2","Dota 2"),("tennis","Теннис"),("basketball","Баскетбол"),("mma","MMA")]]
@app.get("/health")
def health(): return {"status":"ok","mode":"demo"}
@app.get("/sports")
def sports(): return SPORTS
@app.get("/events")
def events(sport:str="football"): return {"sport":sport,"mode":"demo","events":[]}
