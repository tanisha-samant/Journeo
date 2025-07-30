'use client'

import React, { useState } from 'react'
import { FileText, Globe, Download, Share2 } from 'lucide-react'

interface ItinerarySectionProps {
  itinerary: string
  translatedItinerary?: string
}

const ItinerarySection: React.FC<ItinerarySectionProps> = ({ itinerary, translatedItinerary }) => {
  const [showTranslated, setShowTranslated] = useState(false)

  const formatItinerary = (text: string) => {
    // Convert markdown-like formatting to HTML
    return text
      .split('\n')
      .map((line, index) => {
        if (line.startsWith('# ')) {
          return `<h1 class="text-2xl font-bold text-gray-900 mt-6 mb-4">${line.substring(2)}</h1>`
        }
        if (line.startsWith('## ')) {
          return `<h2 class="text-xl font-semibold text-gray-800 mt-4 mb-2">${line.substring(3)}</h2>`
        }
        if (line.startsWith('**') && line.endsWith('**')) {
          return `<p class="font-semibold text-gray-800 mb-2">${line.substring(2, line.length - 2)}</p>`
        }
        if (line.startsWith('- ')) {
          return `<li class="ml-4 mb-1">${line.substring(2)}</li>`
        }
        if (line.trim() === '') {
          return '<br>'
        }
        return `<p class="text-gray-700 mb-2">${line}</p>`
      })
      .join('')
  }

  const downloadItinerary = () => {
    const content = showTranslated ? translatedItinerary : itinerary
    const blob = new Blob([content], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'trip-itinerary.txt'
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  const shareItinerary = async () => {
    if (navigator.share) {
      try {
        await navigator.share({
          title: 'My Trip Itinerary',
          text: showTranslated ? translatedItinerary : itinerary,
        })
      } catch (error) {
        console.log('Error sharing:', error)
      }
    } else {
      // Fallback: copy to clipboard
      const content = showTranslated ? translatedItinerary : itinerary
      navigator.clipboard.writeText(content)
      alert('Itinerary copied to clipboard!')
    }
  }

  return (
    <div className="space-y-6">
      {/* Header with Actions */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <FileText className="h-6 w-6 text-primary-600" />
          <h3 className="text-xl font-bold text-gray-900">Your Itinerary</h3>
        </div>
        
        <div className="flex items-center space-x-2">
          {translatedItinerary && (
            <button
              onClick={() => setShowTranslated(!showTranslated)}
              className="btn-secondary"
            >
              <Globe className="h-4 w-4 mr-2" />
              {showTranslated ? 'Show Original' : 'Show Translated'}
            </button>
          )}
          
          <button
            onClick={downloadItinerary}
            className="btn-secondary"
          >
            <Download className="h-4 w-4 mr-2" />
            Download
          </button>
          
          <button
            onClick={shareItinerary}
            className="btn-secondary"
          >
            <Share2 className="h-4 w-4 mr-2" />
            Share
          </button>
        </div>
      </div>

      {/* Itinerary Content */}
      <div className="bg-white border border-gray-200 rounded-lg p-6 max-h-96 overflow-y-auto">
        <div 
          className="prose prose-sm max-w-none"
          dangerouslySetInnerHTML={{ 
            __html: formatItinerary(showTranslated ? translatedItinerary! : itinerary) 
          }}
        />
      </div>

      {/* Tips Section */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <h4 className="text-lg font-semibold text-blue-900 mb-2">💡 Travel Tips</h4>
        <ul className="text-blue-800 space-y-1">
          <li>• Keep a copy of your itinerary on your phone</li>
          <li>• Research local customs and etiquette</li>
          <li>• Learn basic phrases in the local language</li>
          <li>• Keep emergency contacts handy</li>
          <li>• Stay hydrated and well-rested</li>
        </ul>
      </div>

      {/* Language Note */}
      {translatedItinerary && (
        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
          <p className="text-yellow-800 text-sm">
            <strong>Note:</strong> This is an AI-generated translation. For important information, 
            please verify with local sources or official websites.
          </p>
        </div>
      )}
    </div>
  )
}

export default ItinerarySection 