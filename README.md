# weather_bot

Enter your api in places, start bot and just say "погода в %city name%". At this point works only on Russian cities. 

Uses Wit.ai (https://wit.ai/) as cloud speech recognizer, pymorphy2 (https://pymorphy2.readthedocs.io/en/latest/) as words normalizer and speech recognition library (https://pypi.org/project/SpeechRecognition/) to get speech. 

##  install & run instructions 

* create venv if needed 
  `$ python3 -m venv /path/to/new/virtual/environment`

* activate venv 
  `$ source venv/bin/activate`

* install requirements
  `(venv)$ pip install -r requirements.txt`

* start bot in venv
  `(venv)$ python weather_bot.py
