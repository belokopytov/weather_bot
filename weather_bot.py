import speech_recognition as sr
import requests
import json
import pymorphy2


# weather test 
def get_weather(city_name: str):

    api_key = "api key here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric&lang=ru"
    response = requests.get(complete_url) 
    
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 

        print(" Temperature = " +
                        str(current_temperature) + " C"
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity = " +
                        str(current_humidiy) + "%"
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ") 


def get_city(input_data: str):
    morth = pymorphy2.MorphAnalyzer()
    p = morth.parse(input_data.split(' ')[-1])[0].normal_form
    print(p)
    return p

def main_handler():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Wit.ai
    WIT_AI_KEY = "api key here"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        res = r.recognize_wit(audio, key=WIT_AI_KEY)
        print("Wit.ai thinks you said " + res)
        
        if res.split(' ')[0] == 'погода':
            city = get_city(res)
            print('Запрашиваю погоду в городе ' + city + '...')
            get_weather(city)

    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))

if __name__ == "__main__":
    main_handler()
