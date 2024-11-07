# cintel-06-custom
Kersha's Local Weather Data
Kersha's Local Weather Data Shiny App
This Shiny app is designed to provide current weather information for selected parishes in Louisiana. The application uses data from the OpenWeatherMap API to fetch weather information and provides insights such as current temperature, average temperature, and temperature trends for the selected region. The interface is built using the shiny package for Python and styled with custom CSS.

Table of Contents
Project Overview
Features
Installation
Usage
File Structure
Code Explanation
Requirements
API Key Setup
Contributing
License
Project Overview
Kersha's Local Weather Data app is a Shiny app that allows users to:

Select a parish in Louisiana to view current weather conditions.
Display current temperature and average temperature for the selected parish.
Generate temperature trend plots over time using historical data.
Access external links to related resources and GitHub repositories.
The app uses OpenWeatherMap for real-time data and provides a visually appealing and interactive interface.

Features
Parish Selection: Users can select from East Baton Rouge, Orleans, Lafayette, or Caddo parishes to view weather data.
Current Temperature: Displays the latest temperature for the selected parish.
Temperature Trends: Plots historical temperature data for the selected parish.
Links to External Resources: Provides links to additional resources, including a GitHub repository for further exploration.
Custom Styling: Uses custom CSS for styling, including font settings, color schemes, and icons.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/kersha0530/cintel-06-custom
cd cintel-06-custom
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Install PyShiny and additional required libraries if necessary:

bash
Copy code
pip install shiny shiny-express faicons matplotlib scipy requests
Usage
Make sure your OpenWeatherMap API key is correctly set up in the script (see API Key Setup).
Run the Shiny app:
bash
Copy code
shiny run --reload --launch-browser dashboard/app.py
The app will open in your default web browser.
File Structure
plaintext
Copy code
- dashboard/
  - app.py              # Main application script
- C:\Users\kbrou\OneDrive\Documents\temperature_plot.png  # Saved temperature plot
- requirements.txt      # List of dependencies
- README.md             # This README file
Code Explanation
API Key Setup
API_KEY: This is your OpenWeatherMap API key, which is necessary to fetch weather data. Replace the placeholder with your actual API key.
Function: get_weather_data(lat, lon)
Makes an API request to OpenWeatherMap and returns JSON data.
UI Components
Page Options: Sets up the page title and enables a fillable layout.
Custom CSS: Styles the app, including background color, font settings, and custom classes for headers and images.
Sidebar: Contains components for the app, including the parish selection dropdown, images, and external links.
Main Content: Displays current temperature and temperature trend plots.
Reactive and Render Functions
reactive_calc_combined(): A reactive function that simulates live data updates.
display_temp(): Displays the current temperature for the selected parish.
display_time(): Displays the current timestamp.
display_avg_temp(): Calculates and displays the average temperature.
temperature_plot(): Generates a plot of temperature trends and saves it as an image.
Requirements
Below is the content of requirements.txt:

plaintext
Copy code
shiny
shiny-express
faicons
matplotlib
scipy
requests
API Key Setup
You must obtain an API key from OpenWeatherMap and add it to the script:

python
Copy code
API_KEY = 'your_openweathermap_api_key_here'
Replace 'your_openweathermap_api_key_here' with your actual API key.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

