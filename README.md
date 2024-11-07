# cintel-06-custom
# Kersha's Local Weather Data Shiny App

## Project Overview
Kersha's Local Weather Data app is a Shiny app that provides users with current weather information for selected parishes in Louisiana. The app fetches weather data from the OpenWeatherMap API and displays insights such as:

- Current temperature
- Average temperature
- Temperature trends over time for the selected parish

The interface is built using the Shiny package for Python and is styled with custom CSS to enhance user experience.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Code Explanation](#code-explanation)
- [Requirements](#requirements)
- [API Key Setup](#api-key-setup)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Parish Selection**: Users can select from East Baton Rouge, Orleans, Lafayette, or Caddo parishes to view weather data.
- **Current Temperature**: Displays the latest temperature for the selected parish.
- **Temperature Trends**: Plots historical temperature data for the selected parish.
- **Links to External Resources**: Provides links to additional resources, including a GitHub repository for further exploration.
- **Custom Styling**: Uses custom CSS for styling, including font settings, color schemes, and icons.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kersha0530/cintel-06-custom
   cd cintel-06-custom
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt

3. Install PyShiny and additional required libraries if necessary:
   ```bash
   pip install shiny shiny-express faicons matplotlib scipy requests


# Usage
* Make sure your OpenWeatherMap API key is correctly set up in the script (see API Key Setup).
* Run the Shiny app:
  ```bash
   shiny run --reload --launch-browser dashboard/app.py
-The app will open in your default web browser.

# File Structure
- dashboard/
  - app.py              # Main application script
- C:\Users\kbrou\OneDrive\Documents\temperature_plot.png  # Saved temperature plot
- requirements.txt      # List of dependencies
- README.md             # This README file

# Code Explanation
* API Key Setup
API_KEY: This is your OpenWeatherMap API key, which is necessary to fetch weather data. Replace the placeholder with your actual API key.

* Function: get_weather_data(lat, lon)
Makes an API request to OpenWeatherMap and returns JSON data.

* UI Components
Page Options: Sets up the page title and enables a fillable layout.

* Custom CSS: Styles the app, including background color, font settings, and custom classes for headers and images.

* Sidebar: Contains components for the app, including the parish selection dropdown, images, and external links.

* Main Content: Displays current temperature and temperature trend plots.

* Reactive and Render Functions
- reactive_calc_combined(): A reactive function that simulates live data updates.

- display_temp(): Displays the current temperature for the selected parish.

- display_time(): Displays the current timestamp.

- display_avg_temp(): Calculates and displays the average temperature.

- temperature_plot(): Generates a plot of temperature trends and saves it as an image.

# Requirements
Below is the content of requirements.txt:

*shiny
*shiny-express
*faicons
*matplotlib
*scipy
*requests

# API Key Setup
- You must obtain an API key from OpenWeatherMap and add it to the script:
  ```bash
   API_KEY = 'your_openweathermap_api_key_here'
-Replace 'your_openweathermap_api_key_here' with your actual API key.

# Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

# License
This project is open-source and available under the MIT License. See the LICENSE file for more details.







