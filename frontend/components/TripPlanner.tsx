'use client'

import React, { useState } from 'react'
import TripForm from './TripForm'
import TripResults from './TripResults'
import { TripData, TripResult } from '../types/trip'

const TripPlanner = () => {
  const [tripResult, setTripResult] = useState<TripResult | null>(null)
  const [loading, setLoading] = useState(false)

  const handlePlanTrip = async (tripData: TripData) => {
    setLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/trips/plan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(tripData),
      })

      if (!response.ok) {
        throw new Error('Failed to plan trip')
      }

      const result = await response.json()
      setTripResult(result)
    } catch (error) {
      console.error('Error planning trip:', error)
      // Show error message to user
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-6xl mx-auto">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div>
          <TripForm onPlanTrip={handlePlanTrip} loading={loading} />
        </div>
        <div>
          {tripResult && <TripResults tripResult={tripResult} />}
        </div>
      </div>
    </div>
  )
}

export default TripPlanner 