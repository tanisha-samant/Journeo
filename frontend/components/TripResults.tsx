'use client'

import React, { useState } from 'react'
import { TripResult } from '../types/trip'
import WeatherWidget from './WeatherWidget'
import CurrencyCard from './CurrencyCard'
import ItinerarySection from './ItinerarySection'
import MapView from './MapView'

interface TripResultsProps {
  tripResult: TripResult
}

const TripResults: React.FC<TripResultsProps> = ({ tripResult }) => {
  const [activeTab, setActiveTab] = useState('itinerary')

  const tabs = [
    { id: 'itinerary', label: 'Itinerary', icon: '📋' },
    { id: 'weather', label: 'Weather', icon: '🌤️' },
    { id: 'currency', label: 'Currency', icon: '💰' },
    { id: 'map', label: 'Map', icon: '🗺️' }
  ]

  return (
    <div className="card">
      <div className="flex items-center space-x-2 mb-6">
        <span className="text-2xl">✨</span>
        <h2 className="text-2xl font-bold text-gray-900">Your Trip Plan</h2>
      </div>

      {/* Tab Navigation */}
      <div className="flex space-x-1 mb-6 bg-gray-100 p-1 rounded-lg">
        {tabs.map(tab => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors ${
              activeTab === tab.id
                ? 'bg-white text-primary-600 shadow-sm'
                : 'text-gray-600 hover:text-gray-900'
            }`}
          >
            <span className="mr-2">{tab.icon}</span>
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="min-h-[400px]">
        {activeTab === 'itinerary' && (
          <ItinerarySection 
            itinerary={tripResult.itinerary}
            translatedItinerary={tripResult.translated_itinerary}
          />
        )}
        
        {activeTab === 'weather' && (
          <WeatherWidget 
            weather={tripResult.weather}
            forecast={tripResult.forecast}
          />
        )}
        
        {activeTab === 'currency' && tripResult.currency_info && (
          <CurrencyCard currencyData={tripResult.currency_info} />
        )}
        
        {activeTab === 'map' && (
          <MapView 
            source={tripResult.weather.city} // Using destination for map
            destination={tripResult.weather.city}
          />
        )}
      </div>

      {/* Trip ID */}
      <div className="mt-6 pt-4 border-t border-gray-200">
        <p className="text-sm text-gray-500">
          Trip ID: {tripResult.trip_id}
        </p>
      </div>
    </div>
  )
}

export default TripResults 