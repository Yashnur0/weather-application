from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

#Backend-Code
#API url
url_ofmy_api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

#calling the text file

text_api_key = ConfigParser()
text_api_key.read("weathar.txt")

#indexing the textfile and the api key
api_pass = text_api_key['my_api_pass'] ['pass']

#calling out the json data from the api
def detect_weather(location):
    done = requests.get(url_ofmy_api.format(location, api_pass))
    if done:
        jason_data = done.json()
        locate = jason_data['name']
        country = jason_data['sys']['country']
        temp_inkelv = jason_data['main']['temp']
        temp_inc = temp_inkelv - 273.15
        temp_inf  = (temp_inkelv * 9/5) - 459.67
        weather_situation = jason_data['weather'][0]['description']
        show_weather = jason_data['weather'][0]['main']
        outcome = (locate, country, temp_inc, temp_inf, weather_situation , show_weather)
        return outcome
    else:
        return None

#formating the data
def weather_take():
    location = enter_city.get()
    situation = detect_weather(location)
    if situation:
        enter_location['text'] = '{}, {}'.format(situation[0], situation[1])
        temperature_label['text'] = '{:.1f}°C, {:.1f}°F'.format(situation[2], situation[3])
        weather_like ['text'] = situation[4]
    else:
        messagebox.showerror("Error", "City cannot be found, Look up a valid city")


# create a tkinter window & set the title & a baground color
mywindow = Tk()
mywindow.title("Global Weather App")
mywindow.configure(background='purple')

#set dimensions of the window
mywindow.geometry("900x500")

#these are inbuilt functions of python which are used to create a text box
enter_city = StringVar()
city = Entry(mywindow, textvariable = enter_city, width=30, bg="gold", fg="black", font=("Arial", 40, "italic"), justify=CENTER,)
city.pack(pady=10)

#inbuilt function of python which is used to create search a button 
find_weather = Button(mywindow, text = "Find Weather", width = 20, bg="white", fg = "blue", font = ("Arial", 30, "italic"), command = weather_take)
find_weather.pack(pady=10)

#this is used to point out you location
enter_location = Label(mywindow, text="", width=0, bg="red", fg="light blue", font=("Arial", 30, "italic"))
enter_location.pack(pady=10)

#prints out the temperature of the city searched
temperature_label = Label(mywindow, text="", width=0, bg="light green", fg="black", font=("Arial", 30, "italic"))
temperature_label.pack(pady=10)

#prints out the weather of the city searched
weather_like = Label(mywindow, text="", width=0, bg="light blue", fg="brown", font=("Arial", 30, "italic"))
weather_like.pack(pady=10)


#finish out the loop
mywindow.mainloop()


