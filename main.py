import platform
import os
import tkinter
from datetime import datetime

import requests
from PIL import ImageTk, Image
from dotenv import load_dotenv

load_dotenv()


FONT = 'Futura'
WINDOW_DIM = "580x535"
BUTTON_FONT_SIZE = 32
BUTTON_IPADX = 0


if platform.system() == "Windows":
    FONT = 'Bahnschrift SemiBold SemiConden'
    WINDOW_DIM = "640x600"
    BUTTON_FONT_SIZE = 19
    BUTTON_IPADX = 10


def weather_api_connection(city):
    par = {'q': city,
           'appid': os.getenv('appid'),
           'units': 'metric'}

    return requests.get('http://api.openweathermap.org/data/2.5/weather', params=par)


def temp(city):
    response = weather_api_connection(city)
    return f"{response.json()['main']['temp']}°C"


def clouds(city):
    response = weather_api_connection(city)
    return response.json()['weather'][0]['main']


def humidity(city):
    response = weather_api_connection(city)
    return f"{response.json()['main']['humidity']}%"


def sunrise(city):
    response = weather_api_connection(city)
    return datetime.fromtimestamp(response.json()['sys']['sunrise']).strftime('%X')[:-3] + '   '


def sunset(city):
    response = weather_api_connection(city)
    return datetime.fromtimestamp(response.json()['sys']['sunset']).strftime('%X')[:-3]


window = tkinter.Tk()
window.title("WeatherCool")
window.geometry(WINDOW_DIM)

tkinter.Label(window, text="What's the weather in:", font=(FONT, 52)).pack(pady=10)

entry_frame = tkinter.Frame(window)

entry = tkinter.Entry(entry_frame, font=(FONT, 30))
entry.insert(0, 'Enter city name')
entry.pack(side='left')


def on_click(event):
    entry.delete(0, tkinter.END)
    entry.unbind('<Button-1>', on_click_id)


on_click_id = entry.bind('<Button-1>', on_click)


def click_action():
    temp_label.config(text=temp(entry.get()))
    clouds_label.config(text=clouds(entry.get()))
    humidity_label.config(text=humidity(entry.get()))
    sunrise_label.config(text=sunrise(entry.get()))
    sunset_label.config(text=sunset(entry.get()))
    canvas_temp.create_image(0, 3, anchor=tkinter.NW, image=img_temp)
    canvas_clouds.create_image(0, 3, anchor=tkinter.NW, image=img_clouds)
    canvas_humidity.create_image(0, 3, anchor=tkinter.NW, image=img_humidity)
    canvas_sunrise.create_image(0, 3, anchor=tkinter.NW, image=img_sunrise)
    canvas_sunset.create_image(0, 3, anchor=tkinter.NW, image=img_sunset)


def enter_click_action(event):
    click_action()


window.bind('<Return>', enter_click_action)

button = tkinter.Button(entry_frame, text="🔍", font=(FONT, BUTTON_FONT_SIZE), command=click_action)
button.pack(pady=10, ipadx=BUTTON_IPADX, side='left')

entry_frame.pack()

temp_frame = tkinter.Frame(window)
temp_frame.pack(pady=5)
canvas_temp = tkinter.Canvas(temp_frame, width=68, height=68)
canvas_temp.pack(side='left')
img = Image.open("resources/temp.png")
img_temp = ImageTk.PhotoImage(img)


clouds_frame = tkinter.Frame(window)
clouds_frame.pack(pady=5)
canvas_clouds = tkinter.Canvas(clouds_frame, width=68, height=68)
canvas_clouds.pack(side='left')
img = Image.open("resources/cloudy.png")
img_clouds = ImageTk.PhotoImage(img)


humidity_frame = tkinter.Frame(window)
humidity_frame.pack(pady=5)
canvas_humidity = tkinter.Canvas(humidity_frame, width=68, height=68)
canvas_humidity.pack(side='left')
img = Image.open("resources/drops.png")
img_humidity = ImageTk.PhotoImage(img)


temp_label = tkinter.Label(temp_frame, font=(FONT, 40))
temp_label.pack(pady=5, side='left')
clouds_label = tkinter.Label(clouds_frame, font=(FONT, 40))
clouds_label.pack(pady=5, side='left')
humidity_label = tkinter.Label(humidity_frame, font=(FONT, 40))
humidity_label.pack(pady=5, side='left')


sun_frame = tkinter.Frame(window)
sun_frame.pack(pady=5, )
canvas_sunrise = tkinter.Canvas(sun_frame, width=68, height=68)
canvas_sunset = tkinter.Canvas(sun_frame, width=68, height=68)
img = Image.open("resources/sunrise.png")
img_sunrise = ImageTk.PhotoImage(img)
img = Image.open("resources/sunset.png")
img_sunset = ImageTk.PhotoImage(img)

sunrise_label = tkinter.Label(sun_frame, font=(FONT, 40))
sunset_label = tkinter.Label(sun_frame, font=(FONT, 40))


canvas_sunrise.pack(side='left')
sunrise_label.pack(pady=5, side='left')
canvas_sunset.pack(side='left')
sunset_label.pack(pady=5, side='left')

window.mainloop()
