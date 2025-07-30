'use client'

import React, { useEffect, useRef } from 'react'
import { MapPin, Navigation } from 'lucide-react'

interface MapViewProps {
  source: string
  destination: string
}

const MapView: React.FC<MapViewProps> = ({ source, destination }) => {
  const mapRef = useRef<HTMLDivElement>(null)
  const mapInstanceRef = useRef<any>(null)

  useEffect(() => {
    // Dynamically import Leaflet to avoid SSR issues
    const initMap = async () => {
      if (typeof window !== 'undefined' && mapRef.current) {
        const L = await import('leaflet')
        
        // Import Leaflet CSS
        if (!document.querySelector('link[href*="leaflet.css"]')) {
          const link = document.createElement('link')
          link.rel = 'stylesheet'
          link.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css'
          document.head.appendChild(link)
        }

        // Initialize map
        if (!mapInstanceRef.current) {
          mapInstanceRef.current = L.map(mapRef.current).setView([40.7128, -74.0060], 10)
          
          // Add OpenStreetMap tiles
          L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
          }).addTo(mapInstanceRef.current)

          // Add markers for source and destination
          const sourceMarker = L.marker([40.7128, -74.0060]).addTo(mapInstanceRef.current)
          sourceMarker.bindPopup(`<b>From:</b> ${source}`)

          const destMarker = L.marker([40.7589, -73.9851]).addTo(mapInstanceRef.current)
          destMarker.bindPopup(`<b>To:</b> ${destination}`)

          // Draw route line (mock route)
          const routeLine = L.polyline([
            [40.7128, -74.0060],
            [40.7589, -73.9851]
          ], { color: '#3b82f6', weight: 4 }).addTo(mapInstanceRef.current)

          // Fit map to show both markers
          const group = L.featureGroup([sourceMarker, destMarker, routeLine])
          mapInstanceRef.current.fitBounds(group.getBounds().pad(0.1))
        }
      }
    }

    initMap()

    // Cleanup
    return () => {
      if (mapInstanceRef.current) {
        mapInstanceRef.current.remove()
        mapInstanceRef.current = null
      }
    }
  }, [source, destination])

  return (
    <div className="space-y-4">
      {/* Map Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <Navigation className="h-6 w-6 text-primary-600" />
          <h3 className="text-xl font-bold text-gray-900">Route Map</h3>
        </div>
        
        <div className="flex items-center space-x-4 text-sm text-gray-600">
          <div className="flex items-center space-x-1">
            <MapPin className="h-4 w-4 text-red-500" />
            <span>From: {source}</span>
          </div>
          <div className="flex items-center space-x-1">
            <MapPin className="h-4 w-4 text-green-500" />
            <span>To: {destination}</span>
          </div>
        </div>
      </div>

      {/* Map Container */}
      <div 
        ref={mapRef} 
        className="w-full h-96 rounded-lg border border-gray-200"
        style={{ minHeight: '400px' }}
      />

      {/* Route Information */}
      <div className="bg-gray-50 rounded-lg p-4">
        <h4 className="text-lg font-semibold text-gray-900 mb-3">Route Information</h4>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="text-center">
            <p className="text-sm text-gray-600">Distance</p>
            <p className="text-xl font-bold text-gray-900">~5.2 km</p>
          </div>
          <div className="text-center">
            <p className="text-sm text-gray-600">Duration</p>
            <p className="text-xl font-bold text-gray-900">~15 min</p>
          </div>
          <div className="text-center">
            <p className="text-sm text-gray-600">Transport</p>
            <p className="text-xl font-bold text-gray-900">Car</p>
          </div>
        </div>
      </div>

      {/* Transport Options */}
      <div>
        <h4 className="text-lg font-semibold text-gray-900 mb-3">Transport Options</h4>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          <div className="bg-white border border-gray-200 rounded-lg p-3 text-center hover:border-primary-300 transition-colors">
            <div className="text-2xl mb-2">🚗</div>
            <p className="font-medium text-gray-900">Car</p>
            <p className="text-sm text-gray-600">15 min</p>
          </div>
          <div className="bg-white border border-gray-200 rounded-lg p-3 text-center hover:border-primary-300 transition-colors">
            <div className="text-2xl mb-2">🚇</div>
            <p className="font-medium text-gray-900">Subway</p>
            <p className="text-sm text-gray-600">25 min</p>
          </div>
          <div className="bg-white border border-gray-200 rounded-lg p-3 text-center hover:border-primary-300 transition-colors">
            <div className="text-2xl mb-2">🚶</div>
            <p className="font-medium text-gray-900">Walking</p>
            <p className="text-sm text-gray-600">1h 5min</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default MapView 