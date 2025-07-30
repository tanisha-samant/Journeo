# Journeo - AI-Powered Travel Planner

## 🎯 Project Overview

Journeo is a full-stack web application that leverages AI to create personalized travel itineraries. The application combines multiple APIs to provide a comprehensive travel planning experience with real-time weather data, currency conversion, interactive maps, and multi-language support.

## 🏗️ Architecture

### Backend (FastAPI + Python)
- **Framework**: FastAPI with automatic API documentation
- **Database**: PostgreSQL with SQLAlchemy ORM (SQLite for development)
- **AI Integration**: CrewAI + Groq API for intelligent itinerary generation
- **APIs Integrated**:
  - OpenWeatherMap API (weather data)
  - ExchangeRate.host API (currency conversion)
  - LibreTranslate.de API (translation)
  - OpenRouteService API (route planning)
  - Overpass API (accommodation search)

### Frontend (Next.js + React)
- **Framework**: Next.js 14 with TypeScript
- **Styling**: Tailwind CSS with custom components
- **Maps**: Leaflet.js with OpenStreetMap tiles
- **Charts**: Chart.js for weather and currency visualization
- **Icons**: Lucide React for consistent iconography

## 🚀 Key Features

### 1. AI-Powered Itinerary Generation
- Uses CrewAI with specialized agents (Travel Researcher, Itinerary Planner, Budget Advisor)
- Generates personalized day-by-day schedules
- Considers budget, travel type, and user preferences
- Provides cost estimates and budget-friendly alternatives

### 2. Real-time Weather Integration
- Current weather conditions for destination
- 5-day weather forecast with Chart.js visualization
- Sunrise/sunset times and weather details
- Responsive weather widgets with animated icons

### 3. Currency Conversion
- Real-time exchange rates from 10+ currencies
- Interactive currency converter
- Historical rate tracking
- Visual currency trends

### 4. Interactive Maps
- Leaflet.js integration with OpenStreetMap
- Route visualization between source and destination
- Multiple transport mode options
- Responsive map components

### 5. Multi-language Support
- AI-generated itinerary translation
- Support for 6+ languages
- Language detection capabilities
- Toggle between original and translated content

### 6. Accommodation Search
- Hotel and guesthouse discovery
- Location-based search
- Amenity filtering
- Contact information and ratings

## 📁 Project Structure

```
Journeo/
├── backend/                     # FastAPI Backend
│   ├── app/
│   │   ├── config.py           # Configuration management
│   │   ├── main.py             # FastAPI application
│   │   ├── models/             # Database models
│   │   ├── routers/            # API endpoints
│   │   ├── schemas/            # Pydantic schemas
│   │   └── services/           # Business logic services
│   ├── requirements.txt        # Python dependencies
│   └── env.example            # Environment variables template
├── frontend/                    # Next.js Frontend
│   ├── app/
│   │   ├── globals.css         # Global styles
│   │   ├── layout.tsx          # Root layout
│   │   └── page.tsx            # Main page
│   ├── components/             # React components
│   ├── types/                  # TypeScript definitions
│   └── package.json            # Node.js dependencies
├── README.md                   # Project documentation
├── setup.md                    # Setup guide
├── start.sh                    # Linux/Mac startup script
└── start.bat                   # Windows startup script
```

## 🔧 Technical Implementation

### Backend Services

1. **AIService** (`ai_service.py`)
   - CrewAI integration with Groq API
   - Multi-agent workflow for itinerary generation
   - Fallback to mock data when API unavailable

2. **WeatherService** (`weather_service.py`)
   - OpenWeatherMap API integration
   - Current weather and forecast data
   - Mock data fallback

3. **CurrencyService** (`currency_service.py`)
   - ExchangeRate.host API integration
   - Real-time currency conversion
   - Historical rate tracking

4. **TranslationService** (`translation_service.py`)
   - LibreTranslate.de API integration
   - Multi-language support
   - Itinerary translation

5. **RouteService** (`route_service.py`)
   - OpenRouteService API integration
   - Multi-modal route planning
   - Geocoding capabilities

6. **AccommodationService** (`accommodation_service.py`)
   - Overpass API integration
   - Hotel and accommodation search
   - Location-based filtering

### Frontend Components

1. **TripPlanner** - Main orchestrator component
2. **TripForm** - User input form with validation
3. **TripResults** - Tabbed results display
4. **WeatherWidget** - Weather information and forecasts
5. **CurrencyCard** - Currency conversion interface
6. **ItinerarySection** - AI-generated itinerary display
7. **MapView** - Interactive map with Leaflet.js

## 🌐 API Endpoints

### Trip Planning
- `POST /api/trips/plan` - Generate AI itinerary
- `GET /api/trips/` - Get all trips
- `GET /api/trips/{id}` - Get specific trip
- `DELETE /api/trips/{id}` - Delete trip

### Weather
- `GET /api/weather/{city}` - Current weather
- `GET /api/weather/{city}/forecast` - Weather forecast
- `POST /api/weather/` - Weather by request

### Currency
- `GET /api/currency/convert` - Currency conversion
- `GET /api/currency/rates` - Exchange rates
- `GET /api/currency/currencies` - Supported currencies

### Translation
- `POST /api/translate/` - Text translation
- `POST /api/translate/itinerary` - Itinerary translation
- `GET /api/translate/languages` - Supported languages

### Routes
- `GET /api/routes/` - Route planning
- `GET /api/routes/multimodal` - Multi-modal routes

### Accommodations
- `GET /api/accommodations/{city}` - Find accommodations

## 🎨 UI/UX Features

### Design System
- **Colors**: Primary blue theme with secondary grays
- **Typography**: Inter font family
- **Components**: Reusable Tailwind CSS classes
- **Responsive**: Mobile-first design approach

### User Experience
- **Progressive Enhancement**: Works without JavaScript
- **Loading States**: Skeleton screens and spinners
- **Error Handling**: Graceful fallbacks and user feedback
- **Accessibility**: ARIA labels and keyboard navigation

### Interactive Elements
- **Tabbed Interface**: Organized content sections
- **Form Validation**: Real-time input validation
- **Dynamic Maps**: Interactive route visualization
- **Currency Converter**: Real-time calculations

## 🔒 Security & Performance

### Security
- **CORS Configuration**: Proper cross-origin settings
- **Input Validation**: Pydantic schema validation
- **API Key Management**: Environment variable protection
- **Error Handling**: Secure error responses

### Performance
- **Lazy Loading**: Dynamic imports for heavy components
- **Caching**: API response caching strategies
- **Optimization**: Code splitting and bundle optimization
- **CDN**: External resources from CDNs

## 🚀 Deployment Ready

### Backend Deployment
- **Production Server**: Gunicorn with Uvicorn workers
- **Database**: PostgreSQL with connection pooling
- **Environment**: Docker containerization support
- **Monitoring**: Health check endpoints

### Frontend Deployment
- **Static Export**: Next.js static generation
- **CDN Ready**: Optimized assets for CDN delivery
- **Environment Variables**: Runtime configuration
- **Build Optimization**: Production build process

## 📊 Data Flow

1. **User Input** → TripForm component
2. **API Request** → Backend trip planning endpoint
3. **AI Processing** → CrewAI agents generate itinerary
4. **Data Aggregation** → Multiple API calls for weather, currency, etc.
5. **Response** → Structured data with itinerary and supporting information
6. **UI Rendering** → Tabbed interface with interactive components

## 🔮 Future Enhancements

### Planned Features
- **User Authentication**: JWT-based user accounts
- **Trip History**: Save and manage past trips
- **Social Sharing**: Share itineraries on social media
- **Offline Support**: PWA capabilities
- **Voice Commands**: Speech-to-text input
- **AR Integration**: Augmented reality features

### Technical Improvements
- **Real-time Updates**: WebSocket integration
- **Advanced Caching**: Redis implementation
- **Microservices**: Service decomposition
- **Machine Learning**: Personalized recommendations
- **Analytics**: User behavior tracking

## 🎉 Success Metrics

### User Experience
- **Load Time**: < 3 seconds for initial page load
- **API Response**: < 2 seconds for itinerary generation
- **Uptime**: 99.9% availability target
- **Error Rate**: < 1% API error rate

### Technical Performance
- **Bundle Size**: < 500KB initial JavaScript
- **Lighthouse Score**: > 90 for all metrics
- **API Documentation**: 100% endpoint coverage
- **Test Coverage**: > 80% code coverage

## 📞 Support & Maintenance

### Documentation
- **API Docs**: Auto-generated with FastAPI
- **Setup Guide**: Comprehensive installation instructions
- **Component Docs**: Storybook integration ready
- **Troubleshooting**: Common issues and solutions

### Monitoring
- **Health Checks**: Automated system monitoring
- **Error Tracking**: Centralized error logging
- **Performance Metrics**: Real-time performance monitoring
- **User Analytics**: Usage pattern analysis

---

**Journeo** represents a modern, scalable approach to travel planning that combines the power of AI with real-time data to create personalized, comprehensive travel experiences. The application is built with best practices in mind, ensuring maintainability, scalability, and user satisfaction. 