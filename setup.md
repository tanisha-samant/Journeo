# Journeo - Setup Guide

This guide will help you set up the full-stack AI-powered travel planner application.

## 📋 Prerequisites

- **Node.js 18+** and npm
- **Python 3.11+** and pip
- **PostgreSQL** database (or use SQLite for development)
- **Git** for version control

## 🔑 Required API Keys

Before starting, you'll need to obtain API keys for the following services:

### 1. Groq API (for AI itinerary generation)
- Sign up at: https://console.groq.com/
- Get your API key from the dashboard
- Used for: AI-powered trip planning with CrewAI

### 2. OpenWeatherMap API (for weather data)
- Sign up at: https://openweathermap.org/api
- Get your API key (free tier available)
- Used for: Current weather and forecasts

### 3. OpenRouteService API (for route planning)
- Sign up at: https://openrouteservice.org/
- Get your API key (free tier available)
- Used for: Travel route optimization

### 4. ExchangeRate.host API (for currency conversion)
- Free service at: https://exchangerate.host/
- No API key required for basic usage
- Used for: Real-time currency rates

### 5. LibreTranslate.de API (for translation)
- Free service at: https://libretranslate.de/
- No API key required for basic usage
- Used for: Multi-language support

## 🚀 Quick Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Journeo
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp env.example .env

# Edit .env file with your API keys
# Use your preferred text editor to add your API keys
```

### 3. Configure Environment Variables

Edit the `.env` file in the backend directory:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/journeo_db
# Or use SQLite for development:
# DATABASE_URL=sqlite:///./journeo.db

# JWT Configuration
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API Keys
GROQ_API_KEY=your-groq-api-key-here
OPENWEATHER_API_KEY=your-openweather-api-key-here
OPENROUTE_API_KEY=your-openroute-api-key-here

# External API URLs
EXCHANGERATE_API_URL=https://api.exchangerate.host
LIBRETRANSLATE_API_URL=https://libretranslate.de/translate
OVERPASS_API_URL=https://overpass-api.de/api/interpreter

# Application Settings
DEBUG=True
CORS_ORIGINS=["http://localhost:3000", "http://127.0.0.1:3000"]
```

### 4. Database Setup

#### Option A: PostgreSQL (Recommended for Production)
```bash
# Create database
createdb journeo_db

# Run migrations (if using Alembic)
alembic upgrade head
```

#### Option B: SQLite (Development)
```bash
# The application will automatically create the SQLite database
# No additional setup required
```

### 5. Start Backend Server
```bash
# Make sure you're in the backend directory with venv activated
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at: http://localhost:8000
API documentation: http://localhost:8000/docs

### 6. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at: http://localhost:3000

## 🧪 Testing the Application

### 1. Test Backend APIs
Visit http://localhost:8000/docs to see the interactive API documentation.

Test the health endpoint:
```bash
curl http://localhost:8000/health
```

### 2. Test Frontend
1. Open http://localhost:3000 in your browser
2. Fill out the trip planning form
3. Submit to generate an AI itinerary
4. Explore the different tabs (Itinerary, Weather, Currency, Map)

### 3. Sample Trip Request
```json
{
  "source": "New York",
  "destination": "Paris",
  "start_date": "2024-06-15",
  "end_date": "2024-06-22",
  "budget": 3000,
  "travel_type": "cultural",
  "language": "en"
}
```

## 🔧 Development

### Backend Development
- The backend uses FastAPI with automatic API documentation
- All services have fallback mock data when APIs are unavailable
- Check the logs for any API errors or fallback usage

### Frontend Development
- Built with Next.js 14 and TypeScript
- Uses Tailwind CSS for styling
- Components are modular and reusable
- Leaflet maps are loaded dynamically to avoid SSR issues

### Adding New Features
1. **Backend**: Add new services in `app/services/`
2. **Frontend**: Add new components in `frontend/components/`
3. **API**: Add new endpoints in `app/routers/`

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Check that all API keys are correctly set in `.env`
   - Verify API key permissions and quotas
   - Check the backend logs for specific error messages

2. **Database Connection Issues**
   - Verify PostgreSQL is running
   - Check database credentials in `.env`
   - Try using SQLite for development

3. **Frontend Build Issues**
   - Clear node_modules and reinstall: `rm -rf node_modules && npm install`
   - Check Node.js version compatibility
   - Clear Next.js cache: `rm -rf .next`

4. **CORS Issues**
   - Ensure backend CORS settings include frontend URL
   - Check that both servers are running on correct ports

### Logs and Debugging
- Backend logs: Check terminal where uvicorn is running
- Frontend logs: Check browser developer console
- API errors: Check http://localhost:8000/docs for detailed error responses

## 📚 API Documentation

### Main Endpoints
- `POST /api/trips/plan` - Generate AI itinerary
- `GET /api/weather/{city}` - Get weather data
- `GET /api/currency/convert` - Currency conversion
- `POST /api/translate` - Translate text
- `GET /api/routes/` - Get travel routes
- `GET /api/accommodations/{city}` - Find accommodations

### Interactive Documentation
Visit http://localhost:8000/docs for full API documentation with testing interface.

## 🚀 Deployment

### Backend Deployment
1. Set up a production database (PostgreSQL recommended)
2. Configure environment variables for production
3. Use a production ASGI server like Gunicorn
4. Set up reverse proxy (nginx) for SSL termination

### Frontend Deployment
1. Build the application: `npm run build`
2. Deploy to Vercel, Netlify, or your preferred hosting service
3. Configure environment variables for production API endpoints

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the API documentation at http://localhost:8000/docs
3. Check the application logs for error messages
4. Ensure all API keys are valid and have sufficient quotas

## 🎉 Success!

Once both servers are running and you can access the application, you have successfully set up Journeo! The application will provide:

- AI-generated travel itineraries
- Real-time weather information
- Currency conversion
- Interactive maps
- Multi-language support
- Accommodation search

Enjoy planning your trips with AI! ✈️ 