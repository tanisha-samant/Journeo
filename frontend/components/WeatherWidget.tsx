'use client'

import React from 'react'
import { WeatherData, ForecastData } from '../types/trip'
import { Cloud, Sun, Wind, Droplets, Thermometer } from 'lucide-react'

interface WeatherWidgetProps {
  weather: WeatherData
  forecast: ForecastData
}

const WeatherWidget: React.FC<WeatherWidgetProps> = ({ weather, forecast }) => {
  const formatTime = (timestamp: number) => {
    return new Date(timestamp * 1000).toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  const getWeatherIcon = (icon: string) => {
    const iconMap: Record<string, string> = {
      '01d': '☀️',
      '01n': '🌙',
      '02d': '⛅',
      '02n': '☁️',
      '03d': '☁️',
      '03n': '☁️',
      '04d': '☁️',
      '04n': '☁️',
      '09d': '🌧️',
      '09n': '🌧️',
      '10d': '🌦️',
      '10n': '🌧️',
      '11d': '⛈️',
      '11n': '⛈️',
      '13d': '❄️',
      '13n': '❄️',
      '50d': '🌫️',
      '50n': '🌫️'
    }
    return iconMap[icon] || '🌤️'
  }

  return (
    <div className="space-y-6">
      {/* Current Weather */}
      <div className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg p-6 text-white">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-2xl font-bold">{weather.city}</h3>
            <p className="text-blue-100">{weather.country}</p>
            <div className="flex items-center mt-2">
              <span className="text-4xl font-bold">{Math.round(weather.temperature)}°C</span>
              <span className="text-xl ml-2">feels like {Math.round(weather.feels_like)}°C</span>
            </div>
            <p className="text-lg capitalize mt-1">{weather.description}</p>
          </div>
          <div className="text-6xl">
            {getWeatherIcon(weather.icon)}
          </div>
        </div>

        {/* Weather Details */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
          <div className="flex items-center space-x-2">
            <Droplets className="h-5 w-5" />
            <div>
              <p className="text-sm text-blue-100">Humidity</p>
              <p className="font-semibold">{weather.humidity}%</p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <Wind className="h-5 w-5" />
            <div>
              <p className="text-sm text-blue-100">Wind</p>
              <p className="font-semibold">{weather.wind_speed} m/s</p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <Thermometer className="h-5 w-5" />
            <div>
              <p className="text-sm text-blue-100">Pressure</p>
              <p className="font-semibold">{weather.pressure} hPa</p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <Sun className="h-5 w-5" />
            <div>
              <p className="text-sm text-blue-100">Visibility</p>
              <p className="font-semibold">{weather.visibility / 1000} km</p>
            </div>
          </div>
        </div>
      </div>

      {/* 5-Day Forecast */}
      <div>
        <h4 className="text-lg font-semibold text-gray-900 mb-4">5-Day Forecast</h4>
        <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
          {forecast.forecast.slice(0, 5).map((item, index) => (
            <div key={index} className="bg-white border border-gray-200 rounded-lg p-4 text-center">
              <p className="text-sm text-gray-600">
                {new Date(item.datetime * 1000).toLocaleDateString('en-US', { weekday: 'short' })}
              </p>
              <div className="text-2xl my-2">
                {getWeatherIcon(item.icon)}
              </div>
              <p className="font-semibold">{Math.round(item.temperature)}°C</p>
              <p className="text-sm text-gray-600 capitalize">{item.description}</p>
              <p className="text-xs text-gray-500 mt-1">
                {Math.round(item.pop * 100)}% rain
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Sunrise/Sunset */}
      <div className="bg-gray-50 rounded-lg p-4">
        <h4 className="text-lg font-semibold text-gray-900 mb-3">Sun Schedule</h4>
        <div className="flex justify-around">
          <div className="text-center">
            <Sun className="h-8 w-8 text-yellow-500 mx-auto mb-2" />
            <p className="text-sm text-gray-600">Sunrise</p>
            <p className="font-semibold">{formatTime(weather.sunrise)}</p>
          </div>
          <div className="text-center">
            <Sun className="h-8 w-8 text-orange-500 mx-auto mb-2" />
            <p className="text-sm text-gray-600">Sunset</p>
            <p className="font-semibold">{formatTime(weather.sunset)}</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default WeatherWidget 