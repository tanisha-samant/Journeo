'use client'

import React, { useState } from 'react'
import { Calendar, MapPin, DollarSign, Globe, Sparkles } from 'lucide-react'
import { TripData } from '../types/trip'

interface TripFormProps {
  onPlanTrip: (tripData: TripData) => void
  loading: boolean
}

const TripForm: React.FC<TripFormProps> = ({ onPlanTrip, loading }) => {
  const [formData, setFormData] = useState<TripData>({
    source: '',
    destination: '',
    start_date: '',
    end_date: '',
    budget: undefined,
    travel_type: 'general',
    preferences: {},
    language: 'en'
  })

  const travelTypes = [
    { value: 'general', label: 'General' },
    { value: 'budget', label: 'Budget' },
    { value: 'luxury', label: 'Luxury' },
    { value: 'adventure', label: 'Adventure' },
    { value: 'cultural', label: 'Cultural' },
    { value: 'relaxation', label: 'Relaxation' }
  ]

  const languages = [
    { value: 'en', label: 'English' },
    { value: 'es', label: 'Spanish' },
    { value: 'fr', label: 'French' },
    { value: 'de', label: 'German' },
    { value: 'it', label: 'Italian' },
    { value: 'pt', label: 'Portuguese' }
  ]

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    onPlanTrip(formData)
  }

  const handleInputChange = (field: keyof TripData, value: any) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }))
  }

  return (
    <div className="card">
      <div className="flex items-center space-x-2 mb-6">
        <Sparkles className="h-6 w-6 text-primary-600" />
        <h2 className="text-2xl font-bold text-gray-900">Plan Your Trip</h2>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Source and Destination */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <MapPin className="h-4 w-4 inline mr-1" />
              From
            </label>
            <input
              type="text"
              value={formData.source}
              onChange={(e) => handleInputChange('source', e.target.value)}
              placeholder="Enter departure city"
              className="input-field"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <MapPin className="h-4 w-4 inline mr-1" />
              To
            </label>
            <input
              type="text"
              value={formData.destination}
              onChange={(e) => handleInputChange('destination', e.target.value)}
              placeholder="Enter destination city"
              className="input-field"
              required
            />
          </div>
        </div>

        {/* Dates */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <Calendar className="h-4 w-4 inline mr-1" />
              Start Date
            </label>
            <input
              type="date"
              value={formData.start_date}
              onChange={(e) => handleInputChange('start_date', e.target.value)}
              className="input-field"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <Calendar className="h-4 w-4 inline mr-1" />
              End Date
            </label>
            <input
              type="date"
              value={formData.end_date}
              onChange={(e) => handleInputChange('end_date', e.target.value)}
              className="input-field"
              required
            />
          </div>
        </div>

        {/* Budget and Travel Type */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <DollarSign className="h-4 w-4 inline mr-1" />
              Budget (USD)
            </label>
            <input
              type="number"
              value={formData.budget || ''}
              onChange={(e) => handleInputChange('budget', e.target.value ? Number(e.target.value) : undefined)}
              placeholder="Optional"
              className="input-field"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Travel Type
            </label>
            <select
              value={formData.travel_type}
              onChange={(e) => handleInputChange('travel_type', e.target.value)}
              className="input-field"
            >
              {travelTypes.map(type => (
                <option key={type.value} value={type.value}>
                  {type.label}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Language */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            <Globe className="h-4 w-4 inline mr-1" />
            Language for Itinerary
          </label>
          <select
            value={formData.language}
            onChange={(e) => handleInputChange('language', e.target.value)}
            className="input-field"
          >
            {languages.map(lang => (
              <option key={lang.value} value={lang.value}>
                {lang.label}
              </option>
            ))}
          </select>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={loading}
          className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? (
            <div className="flex items-center justify-center">
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
              Planning your trip...
            </div>
          ) : (
            <div className="flex items-center justify-center">
              <Sparkles className="h-4 w-4 mr-2" />
              Generate AI Itinerary
            </div>
          )}
        </button>
      </form>
    </div>
  )
}

export default TripForm 