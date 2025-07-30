export interface TripData {
  source: string
  destination: string
  start_date: string
  end_date: string
  budget?: number
  travel_type?: string
  preferences?: Record<string, any>
  language?: string
}

export interface TripResult {
  trip_id: number
  itinerary: string
  translated_itinerary?: string
  weather: WeatherData
  forecast: ForecastData
  currency_info?: CurrencyData
  success: boolean
}

export interface WeatherData {
  city: string
  country: string
  temperature: number
  feels_like: number
  humidity: number
  pressure: number
  description: string
  icon: string
  wind_speed: number
  wind_direction: number
  visibility: number
  sunrise: number
  sunset: number
}

export interface ForecastData {
  city: string
  country: string
  forecast: ForecastItem[]
}

export interface ForecastItem {
  datetime: number
  temperature: number
  feels_like: number
  humidity: number
  description: string
  icon: string
  wind_speed: number
  pop: number
}

export interface CurrencyData {
  base_currency: string
  date: string
  rates: Record<string, number>
  timestamp?: number
}

export interface RouteData {
  start: string
  end: string
  mode: string
  distance: number
  duration: number
  coordinates: number[][]
  instructions: RouteInstruction[]
  success: boolean
}

export interface RouteInstruction {
  instruction: string
  distance: number
  duration: number
  type: string
}

export interface AccommodationData {
  id: string
  type: string
  name: string
  tourism_type: string
  latitude: number
  longitude: number
  address: {
    street?: string
    housenumber?: string
    postcode?: string
    city?: string
  }
  contact: {
    phone?: string
    website?: string
    email?: string
  }
  amenities: {
    wifi: boolean
    parking: boolean
    breakfast: boolean
  }
  stars?: number
  rooms?: number
} 