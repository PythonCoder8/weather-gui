# weather-gui
A GUI app to find weather information for specific locations using APIs and Python with the CustomTkinter module made by Tom Schimansky (link to repository: https://github.com/TomSchimansky/CustomTkinter).

Note: This program has only been run using python 3.10.5 and has not been run using any other versions, so results may differ using different versions.

## Installing Dependencies
This app relies on the CustomTkinter module and the requests module to function properly.

### CustomTkinter
The CustomTkinter module is a module used for GUI and is a modern-looking version of the tkinter module. It can be installed with pip using this command:
```
pip install customtkinter
```

### Requests
The requests module is required to obtain weather and location information using REST APIs. It can be installed with pip using this command:
```
pip install requests
```

## APIs
This application uses 3 different [OpenWeatherMap](https://openweathermap.org/) APIs to help get weather information. It uses a geocoding API from OpenWeatherMap to get latitude and longitude coordinates. These coordinates are required by their weather API. The app also uses OpenWeatherMap's Ultraviolet (UV) Index API for additional weather information about UV exposure outside.

## Using the App
Using the app is extremely straight forward. You enter the location you want weather information about, entering the city, then the two-letter country code (example: Los Angeles, US).

![image](https://github.com/PythonCoder8/weather-gui/assets/72826534/9e5ab2fa-44d8-4e95-9453-92cd88681bab)

Note: To find weather information about cities in England, country codes UK or EN will not work as their country code is GB.

