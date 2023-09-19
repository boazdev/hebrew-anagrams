from flask import Flask
import json
#from bson import ObjectId
from flask_cors import CORS
from dotenv import load_dotenv
#from enconder import JSONEncoder
#from routers.subscription_router import subscriptions
from routers.anagrams_router import anagrams
#from flask import request
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
#app.json_encoder = JSONEncoder
app.json
CORS(app)
load_dotenv()
app.register_blueprint(anagrams, url_prefix="/anagrams")
print(f'redis config host, port: {os.getenv("REDIS_HOST")} {os.getenv("REDIS_PORT")}')

app.run(port=8080,debug=True) #the CinemaWS will run on port 8080. SubsWS on port 5000