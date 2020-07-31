import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH= 600

# bfbfd8b4b87d663cdcbd127b6527d7d4
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def format_weather(weather):

    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        temp = "{0:.2f}".format((temp-32)/1.8)

        final_str = 'City : %s\nConditions : %s\nTemperature (°C) : %s\n' % (name, desc,temp)
    except:
        final_str = "There was a problem retrieving that weather info"

    return final_str

def get_weather(city):
    weather_key= 'bfbfd8b4b87d663cdcbd127b6527d7d4'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID': weather_key, 'q': city, 'units':'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    print(weather)
    label['text'] = format_weather(weather)

root = tk.Tk()
root.title("Weather Report")

background_img = tk.PhotoImage()
background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n' )

entry = tk.Entry(frame, font=('Courier', 18))
entry.place( relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place( relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n' )

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()


