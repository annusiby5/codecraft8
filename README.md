# flask-daily-quotes

A modern Flask web application that delivers a motivational **Quote of the Day** to inspire users every day. Each quote remains consistent for 24 hours and automatically updates the next day, providing a fresh dose of motivation with a clean and interactive user interface.

## Features

* 📖 Daily motivational quotes
* 🔄 Automatic quote update every 24 hours
* 🎨 Modern glassmorphism UI
* 🔥 Dark red motivational theme
* ✨ Smooth animations and hover effects
* 📱 Responsive design for desktop and mobile devices
* ⚡ Lightweight and easy to deploy

## Project Structure

```text
flask-daily-quotes/
│
├── quotes.py
├── requirements.txt
├── LICENSE
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/flask-daily-quotes.git
cd flask-daily-quotes
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python quotes.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

## How It Works

The application uses the current date to determine which quote is displayed. This ensures that:

* All users see the same quote on a given day.
* The quote remains unchanged throughout the day.
* A new quote is automatically selected when the date changes.

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Jinja

## License

This project is licensed under the MIT License