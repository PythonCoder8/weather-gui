import requests
import customtkinter as ctk
import sys

# Set Window Properties
root = ctk.CTk()
root.title("Weather")
root.geometry("500x280")
root.resizable(0, 0)


text = ctk.CTkLabel(
    root,
    text="Enter a location (city, 2 letter country code)",
)
entry = ctk.CTkEntry(root)
entry.place(x=183, y=55)

response = None


def submit():
    global response
    if response is not None:
        response.destroy()
    location = entry.get()
    try:
        geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid=07bd17841c06fa85ed496a0d84c88073"
        geocoding_response = requests.get(geocoding_url).json()
        uv_url = f"https://api.openuv.io/api/v1/uv?lat={geocoding_response[0]['lat']}&lng={geocoding_response[0]['lon']}"
        uv_headers = {"x-access-token": "53f048104f72a878b9680c669bfd796e"}
        uv_response = requests.get(uv_url, headers=uv_headers).json()
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&appid=ea88811edf412dbd9717bf2446a24097&q={location}"
        weather_response = requests.get(weather_url).json()
    except IndexError:
        response = ctk.CTkLabel(
            root,
            text=f"Error: invalid location input",
            text_color="red",
        )
        search_btn = ctk.CTkButton(
            root,
            text="Enter",
            command=submit,
            height=30,
            width=30,
        )
        response.place(x=178, y=136)
        search_btn.place(x=230, y=95)
        text.place(x=140, y=25)
        root.mainloop()
        sys.exit()

    try:
        current_temp = round(weather_response["main"]["temp"])
        max_temp = round(weather_response["main"]["temp_max"])
        min_temp = round(weather_response["main"]["temp_min"])
        feels_temp = round(weather_response["main"]["feels_like"])
        uv_index = round(uv_response["result"]["uv"])
    except KeyError as k:
        if "quota exceeded" in uv_response:
            response = ctk.CTkLabel(root, text=f"Daily API quota exceeded")
        else:
            response = ctk.CTkLabel(
                root,
                text=f"Error: invalid location input",
                text_color="red",
            )
        search_btn = ctk.CTkButton(
            root, text="Enter", command=submit, height=30, width=30
        )
        response.place(x=178, y=136)
        search_btn.place(x=230, y=95)
        text.place(x=140, y=25)
        root.mainloop()
        sys.exit()

    response = ctk.CTkLabel(
        root,
        text=f"Current Temperature: {current_temp}{chr(176)}C\nHigh Temperature: {max_temp}{chr(176)}C\nLow Temperature: {min_temp}{chr(176)}C\nFeels like: {feels_temp}{chr(176)}C\nUV Exposure: {uv_index}",
    )

    response.place(x=178, y=136)


search_btn = ctk.CTkButton(root, text="Enter", command=submit, height=30, width=30)
search_btn.place(x=230, y=95)
text.place(x=140, y=25)
root.mainloop()
