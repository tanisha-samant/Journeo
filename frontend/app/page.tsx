'use client'

import React, { useState } from 'react'
import TripPlanner from '../components/TripPlanner'
import Header from '../components/Header'
import Footer from '../components/Footer'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-4">
            Plan Your Perfect Trip with
            <span className="text-primary-600"> AI</span>
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Get personalized itineraries, real-time weather updates, currency conversion, 
            and interactive maps all in one place.
          </p>
        </div>
        
        <TripPlanner />
      </main>
      <Footer />
    </div>
  )
} 