# Journeo - AI-Powered Travel Planner

A full-stack web application that helps users plan their trips with AI-generated itineraries, real-time weather data, currency conversion, and interactive maps.

## 🚀 Features

- **AI-Powered Itinerary Generation**: Uses CrewAI + Groq API for personalized trip planning
- **Interactive Maps**: Leaflet.js with OpenStreetMap for route visualization
- **Real-time Weather**: OpenWeatherMap API integration with Chart.js visualization
- **Currency Conversion**: Real-time exchange rates for cost estimation
- **Multi-language Support**: LibreTranslate.de API for itinerary translation
- **Route Planning**: OpenRouteService API for optimal travel routes
- **Accommodation Search**: Overpass API for finding hotels and guesthouses
- **Transport Options**: Scraped flight, train, and bus data comparison

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 14 (React-based with SSR)
- **Styling**: Tailwind CSS
- **Maps**: Leaflet.js with OpenStreetMap
- **Charts**: Chart.js
- **State Management**: React Context + Hooks

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **AI Agent**: CrewAI + Groq API
- **Scraping**: BeautifulSoup + requests
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens

## 📁 Project Structure

```
Journeo/
├── frontend/                 # Next.js application
│   ├── components/          # Reusable UI components
│   ├── pages/              # Next.js pages
│   ├── styles/             # Global styles
│   └── utils/              # Frontend utilities
├── backend/                 # FastAPI application
│   ├── app/                # Main application code
│   ├── models/             # Database models
│   ├── services/           # Business logic
│   └── utils/              # Backend utilities
└── README.md
```

## 🔑 Required API Keys

You'll need to obtain API keys for the following services:

1. **Groq API** (for AI itinerary generation)
   - Sign up at: https://console.groq.com/
   - Used for: AI-powered trip planning

2. **OpenWeatherMap API** (for weather data)
   - Sign up at: https://openweathermap.org/api
   - Used for: Current weather and forecasts

3. **OpenRouteService API** (for route planning)
   - Sign up at: https://openrouteservice.org/
   - Used for: Travel route optimization

4. **ExchangeRate.host API** (for currency conversion)
   - Free tier available at: https://exchangerate.host/
   - Used for: Real-time currency rates

5. **LibreTranslate.de API** (for translation)
   - Free service at: https://libretranslate.de/
   - Used for: Multi-language support

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- PostgreSQL database

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🌐 API Endpoints

### Backend API Routes
- `POST /api/trips/plan` - Generate AI itinerary
- `GET /api/weather/{city}` - Get weather data
- `GET /api/routes/` - Get travel routes
- `GET /api/currency/convert` - Currency conversion
- `POST /api/translate` - Translate text
- `GET /api/accommodations/{city}` - Find accommodations

## 📱 Screenshots

[Coming soon - will be added after implementation]

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details 