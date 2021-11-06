import requests
import tkinter

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
    return response.json()['main']['humidity']


def sunrise(city):
    response = weather_api_connection(city)
    return response.json()['sys']['sunrise']


def sunset(city):
    response = weather_api_connection(city)
    return response.json()['sys']['sunset']


window = tkinter.Tk()
window.title("WeatherCool")
window.geometry("400x400")

tkinter.Label(window, text="What's the weather in:", font=(FONT, 36)).pack(pady=10)

entry_frame = tkinter.Frame(window)

entry = tkinter.Entry(entry_frame, font=(FONT, 22))
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


def enter_click_action(event):
    temp_label.config(text=temp(entry.get()))
    clouds_label.config(text=clouds(entry.get()))
    humidity_label.config(text=humidity(entry.get()))
    sunrise_label.config(text=sunrise(entry.get()))
    sunset_label.config(text=sunset(entry.get()))


window.bind('<Return>', enter_click_action)

button = tkinter.Button(entry_frame, text="Check", font=(FONT, 21), command=click_action)
button.pack(pady=10, side='left')

entry_frame.pack()

temp_label = tkinter.Label(window, font=(FONT, 26))
temp_label.pack(pady=5)
clouds_label = tkinter.Label(window, font=(FONT, 26))
clouds_label.pack(pady=5)
humidity_label = tkinter.Label(window, font=(FONT, 26))
humidity_label.pack(pady=5)
sunrise_label = tkinter.Label(window, font=(FONT, 26))
sunrise_label.pack(pady=5, side='left')
sunset_label = tkinter.Label(window, font=(FONT, 26))
sunset_label.pack(pady=5, side='left')

window.mainloop()
