'use client'

import React from 'react'
import { Plane, Globe, MapPin } from 'lucide-react'

const Header = () => {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="bg-primary-600 p-2 rounded-lg">
              <Plane className="h-6 w-6 text-white" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900">Journeo</h1>
          </div>
          
          <nav className="hidden md:flex items-center space-x-8">
            <a href="#features" className="text-gray-600 hover:text-primary-600 transition-colors">
              Features
            </a>
            <a href="#about" className="text-gray-600 hover:text-primary-600 transition-colors">
              About
            </a>
            <a href="#contact" className="text-gray-600 hover:text-primary-600 transition-colors">
              Contact
            </a>
          </nav>
          
          <div className="flex items-center space-x-4">
            <button className="btn-secondary">
              <Globe className="h-4 w-4 mr-2" />
              Language
            </button>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header 