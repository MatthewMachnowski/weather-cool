import requests
import tkinter
from PIL import ImageTk, Image


FONT = 'Times New Roman'

def weather_api_connection(city):
    par = {'q': city,
           'appid': 'bc12083e70d2d22298c2df1cec7101d9',
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
    return response.json()['sys']['sunrise']


def sunset(city):
    response = weather_api_connection(city)
    return response.json()['sys']['sunset']


window = tkinter.Tk()
window.title("WeatherCool")
window.geometry("550x550")

tkinter.Label(window, text="What's the weather in:", font=(FONT, 52)).pack(pady=10)

entry_frame = tkinter.Frame(window)

entry = tkinter.Entry(entry_frame, font=(FONT, 30))
entry.insert(0, 'Enter city')
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
    canvas.create_image(0, 3, anchor=tkinter.NW, image=img_temp)

def enter_click_action(event):
    temp_label.config(text=temp(entry.get()))
    clouds_label.config(text=clouds(entry.get()))
    humidity_label.config(text=humidity(entry.get()))
    sunrise_label.config(text=sunrise(entry.get()))
    sunset_label.config(text=sunset(entry.get()))
    canvas.create_image(0, 3, anchor=tkinter.NW, image=img_temp)

window.bind('<Return>', enter_click_action)

button = tkinter.Button(entry_frame, text="Check", font=(FONT, 30), command=click_action)
button.pack(pady=10, side='left')

entry_frame.pack()

temp_frame = tkinter.Frame(window)
temp_frame.pack(pady=5)
canvas = tkinter.Canvas(temp_frame, width=68, height=68)
canvas.pack(side='left')
img = Image.open("resources/temp.png")
# img = img.resize((27, 27), Image.)
img_temp = ImageTk.PhotoImage(img)


temp_label = tkinter.Label(temp_frame, font=(FONT, 42))
temp_label.pack(pady=5, side='left')
clouds_label = tkinter.Label(window, font=(FONT, 42))
clouds_label.pack(pady=5)
humidity_label = tkinter.Label(window, font=(FONT, 42))
humidity_label.pack(pady=5)
sunrise_label = tkinter.Label(window, font=(FONT, 26))
sunrise_label.pack(pady=5, side='left')
sunset_label = tkinter.Label(window, font=(FONT, 26))
sunset_label.pack(pady=5, side='left')

window.mainloop()
