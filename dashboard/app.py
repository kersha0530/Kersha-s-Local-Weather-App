import requests
from shiny import reactive, render
from shiny.express import input
from datetime import datetime
import random
from faicons import icon_svg
from shiny.express import ui
from scipy import stats
import matplotlib.pyplot as plt

# Your OpenWeatherMap API key
API_KEY = '4cc0a30163a9737128eb144e1f8d0d84'

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(lat, lon):
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

ui.tags.link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css")

# Example temperature data for each parish
temperature_data = {
    "East Baton Rouge": [random.uniform(20, 30) for _ in range(10)],
    "Orleans": [random.uniform(22, 32) for _ in range(10)],
    "Lafayette": [random.uniform(19, 29) for _ in range(10)],
    "Caddo": [random.uniform(21, 31) for _ in range(10)],
}

# Set page options correctly
ui.page_opts(title="Kersha's Local Weather Data", fillable=True)

# Add CSS for styling
ui.tags.style("""
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap'); /* Cursive font */

    body {
        background-color: #ccffcc;
        font-family: 'Roboto', sans-serif;
    }

    h2 {
        font-family: 'Great Vibes', cursive;
        font-size: 2.5em;
        text-align: center;
        color: darkgreen;
    }

    .center-img {
        display: block;
        margin: auto;
        width: 150px;
    }

    .text-center {
        text-align: center;
    }

    .bold {
        font-weight: bold;
        color: darkgreen;
    }

    p.bold, h6.bold {
        color: darkgreen;
    }
""")

# Sidebar content
with ui.sidebar(open="open"):
    ui.h2("Local Weather", class_="text-center")
    ui.img(
        src="https://cdn11.bigcommerce.com/s-pn30midutw/images/stencil/original/products/909/2591/sbf-118-louisiana-state-bird-%26-flower-magnet__05638.1667577510.jpg",
        alt="Louisiana State Bird and Flower",
        class_="center-img"
    )
    # Wrapping the input_select in a div for styling
    ui.div(
        ui.input_select("parish", "Select Parish", choices=["East Baton Rouge", "Orleans", "Lafayette", "Caddo"]),
        class_="bold"
    )
    ui.div(
        ui.p("Warmer than usual!", class_="bold"),
        ui.tags.i(class_="fas fa-sun", style="font-size: 2em; color: orange;"),
        class_="text-center"
    )
    ui.hr()
    ui.h6("Links:", class_="bold")
    ui.a(
        ui.tags.i(class_="fab fa-github", style="font-size: 1.5em; color: black;"),
        " An Interactive Insight to the Penguin Species of Antarctica",
        href="https://github.com/kersha0530/cintel-04-local",
        target="_blank"
    )
    ui.a(
        ui.tags.i(class_="fab fa-github", style="font-size: 1.5em; color: black;"),
        " Antarctic Temperature Tracker",
        href="kersha0530.github.io/cintel-05-cintel/",
        target="_blank"
    )
    ui.a(
        ui.tags.i(class_="fa-brands fa-github", style="font-size: 1.5em; color: black;"),
        " GitHub Source",
        href="https://github.com/kersha0530/cintel-06-custom",
        target="_blank"
    )
    ui.a(
        ui.tags.i(class_="fas fa-shield-alt", style="font-size: 1.5em; color: darkblue;"),
        " PyShiny",
        href="https://shiny.posit.co/py/",
        target="_blank"
    )

# Main content area (outside the sidebar)
ui.h2("Current Temperature")
ui.p(
    ui.tags.i(class_="fas fa-thermometer-half", style="font-size: 1.5em; color: red;"),
    class_="text-center"
)

@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} °C"

# Function to display current time
@render.text
def display_time():
    """Get the latest reading and return a timestamp string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"

# Function to display average temperature
@render.text
def display_avg_temp():
    """Calculate the average temperature for the selected parish"""
    latest_dictionary_entry = reactive_calc_combined()
    parish = latest_dictionary_entry['parish']
    temps = temperature_data.get(parish, [])
    avg_temp = sum(temps) / len(temps) if temps else None
    return f"Average Temperature: {avg_temp} °C" if avg_temp is not None else "No data available"

# Plot the temperature
def plot_temperature_data(temperature_series, location):
    plt.figure(figsize=(10, 5))
    plt.plot(temperature_series, marker='o')
    plt.title(f'Temperature Trends in {location}')
    plt.xlabel('Time (last readings)')
    plt.ylabel('Temperature (°C)')
    plt.grid()
    plt.tight_layout()
    plt.savefig('C:\\Users\\kbrou\\OneDrive\\Documents\\temperature_plot.png')
    plt.close()

@render.image
def temperature_plot():
    parish = input.parish()  # Get selected parish
    plot_temperature_data(temperature_data[parish], parish)
    return {
        "src": 'C:\\Users\\kbrou\\OneDrive\\Documents\\temperature_plot.png',
        "alt": f"Temperature Trends for {parish}",
        "height": "400px"
    }

# Reactive calculation logic for live updates
@reactive.calc()
def reactive_calc_combined():
    selected_parish = input.parish()
    temp = temperature_data.get(selected_parish, [None])[-1]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_entry = {"temp": temp, "timestamp": timestamp, "parish": selected_parish}
    return latest_entry

def app_server(input, output, session):
    @output
    @render.text
    def display_temp():
        latest_entry = reactive_calc_combined()
        return f"{latest_entry['temp']} °C"
