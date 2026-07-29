# 🌦️ Weather App

A modern, premium‑looking Flask‑based weather web application that fetches real‑time weather data from the **OpenWeatherMap API** and presents it in a sleek, responsive UI.

---

## 🚀 Features
- Search weather by **city name**
- Display:
  - Country code
  - City name
  - Coordinates (Longitude & Latitude)
  - Temperature (Kelvin & Celsius)
  - Pressure
  - Humidity
- Responsive **Bootstrap 5** UI with gradient background and subtle glass‑morphism effects
- Graceful error handling for invalid city searches

---

## 🎨 UI Preview
![Weather App UI](file:///C:/Users/LENOVO/.gemini/antigravity-ide/brain/c79de2df-ed22-4814-99e2-e42e4d09efed/weather_app_ui_mockup_1785322456526.png)

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, Jinja2, Bootstrap 5, custom CSS for gradients and animations
- **API:** OpenWeatherMap

---

## 📦 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Weather-App.git
   cd Weather-App
   ```
2. **Create a virtual environment & install dependencies**
   ```bash
   python -m venv venv
   .\\venv\\Scripts\\activate   # on Windows
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   - Copy the example file and add your OpenWeatherMap API key:
     ```bash
     cp .env.example .env
     # edit .env and set OPENWEATHER_API_KEY=your_api_key
     ```
4. **Run the application**
   ```bash
   python weather.py
   ```
   The app will be available at `http://127.0.0.1:5000`.

---

## ▶️ Usage
- Open the URL in your browser.
- Enter a city name in the search bar.
- View the current weather details displayed on a beautiful card.

---

## 📂 Project Structure
```
Weather-App/
│   weather.py          # Flask backend
│   .env.example        # Example environment variables
│   .env                # Your local env (git‑ignored)
│   requirements.txt    # Python dependencies
│   README.md           # Documentation (this file)
│
└───templates/
    │   index.html     # Jinja2 template for the UI
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License
This project is licensed under the MIT License – see the `LICENSE` file for details.
