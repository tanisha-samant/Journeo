'use client'

import React, { useState } from 'react'
import { CurrencyData } from '../types/trip'
import { DollarSign, TrendingUp, TrendingDown } from 'lucide-react'

interface CurrencyCardProps {
  currencyData: CurrencyData
}

const CurrencyCard: React.FC<CurrencyCardProps> = ({ currencyData }) => {
  const [fromCurrency, setFromCurrency] = useState('USD')
  const [toCurrency, setToCurrency] = useState('EUR')
  const [amount, setAmount] = useState(1)

  const popularCurrencies = [
    { code: 'USD', name: 'US Dollar', symbol: '$' },
    { code: 'EUR', name: 'Euro', symbol: '€' },
    { code: 'GBP', name: 'British Pound', symbol: '£' },
    { code: 'JPY', name: 'Japanese Yen', symbol: '¥' },
    { code: 'CAD', name: 'Canadian Dollar', symbol: 'C$' },
    { code: 'AUD', name: 'Australian Dollar', symbol: 'A$' },
    { code: 'CHF', name: 'Swiss Franc', symbol: 'CHF' },
    { code: 'CNY', name: 'Chinese Yuan', symbol: '¥' },
    { code: 'INR', name: 'Indian Rupee', symbol: '₹' },
    { code: 'BRL', name: 'Brazilian Real', symbol: 'R$' }
  ]

  const getExchangeRate = (from: string, to: string) => {
    if (from === to) return 1
    if (from === currencyData.base_currency) {
      return currencyData.rates[to] || 1
    }
    if (to === currencyData.base_currency) {
      return 1 / (currencyData.rates[from] || 1)
    }
    // Cross rate calculation
    const fromRate = currencyData.rates[from] || 1
    const toRate = currencyData.rates[to] || 1
    return toRate / fromRate
  }

  const convertedAmount = amount * getExchangeRate(fromCurrency, toCurrency)

  return (
    <div className="space-y-6">
      {/* Currency Converter */}
      <div className="bg-gradient-to-r from-green-500 to-emerald-600 rounded-lg p-6 text-white">
        <h3 className="text-xl font-bold mb-4">Currency Converter</h3>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium mb-2">From</label>
            <select
              value={fromCurrency}
              onChange={(e) => setFromCurrency(e.target.value)}
              className="w-full px-3 py-2 rounded-lg bg-white/20 border border-white/30 text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white/50"
            >
              {popularCurrencies.map(currency => (
                <option key={currency.code} value={currency.code} className="text-gray-900">
                  {currency.code} - {currency.name}
                </option>
              ))}
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-2">Amount</label>
            <input
              type="number"
              value={amount}
              onChange={(e) => setAmount(Number(e.target.value))}
              className="w-full px-3 py-2 rounded-lg bg-white/20 border border-white/30 text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white/50"
              placeholder="1"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-2">To</label>
            <select
              value={toCurrency}
              onChange={(e) => setToCurrency(e.target.value)}
              className="w-full px-3 py-2 rounded-lg bg-white/20 border border-white/30 text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white/50"
            >
              {popularCurrencies.map(currency => (
                <option key={currency.code} value={currency.code} className="text-gray-900">
                  {currency.code} - {currency.name}
                </option>
              ))}
            </select>
          </div>
        </div>
        
        <div className="mt-4 p-4 bg-white/20 rounded-lg">
          <div className="text-center">
            <p className="text-sm text-green-100">Converted Amount</p>
            <p className="text-3xl font-bold">
              {convertedAmount.toFixed(2)} {toCurrency}
            </p>
            <p className="text-sm text-green-100 mt-1">
              Rate: 1 {fromCurrency} = {getExchangeRate(fromCurrency, toCurrency).toFixed(4)} {toCurrency}
            </p>
          </div>
        </div>
      </div>

      {/* Exchange Rates Table */}
      <div>
        <h4 className="text-lg font-semibold text-gray-900 mb-4">Current Exchange Rates</h4>
        <div className="bg-white border border-gray-200 rounded-lg overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">Currency</th>
                  <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">Rate</th>
                  <th className="px-4 py-3 text-left text-sm font-medium text-gray-700">Change</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                {popularCurrencies.slice(0, 8).map(currency => {
                  const rate = currencyData.rates[currency.code] || 1
                  const isPositive = Math.random() > 0.5 // Mock data
                  return (
                    <tr key={currency.code} className="hover:bg-gray-50">
                      <td className="px-4 py-3">
                        <div className="flex items-center">
                          <span className="text-lg mr-2">{currency.symbol}</span>
                          <div>
                            <p className="font-medium text-gray-900">{currency.code}</p>
                            <p className="text-sm text-gray-500">{currency.name}</p>
                          </div>
                        </div>
                      </td>
                      <td className="px-4 py-3 text-gray-900 font-medium">
                        {rate.toFixed(4)}
                      </td>
                      <td className="px-4 py-3">
                        <div className={`flex items-center ${isPositive ? 'text-green-600' : 'text-red-600'}`}>
                          {isPositive ? (
                            <TrendingUp className="h-4 w-4 mr-1" />
                          ) : (
                            <TrendingDown className="h-4 w-4 mr-1" />
                          )}
                          <span className="text-sm">
                            {(Math.random() * 2).toFixed(2)}%
                          </span>
                        </div>
                      </td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Last Updated */}
      <div className="text-center text-sm text-gray-500">
        <p>Last updated: {new Date(currencyData.timestamp || Date.now()).toLocaleString()}</p>
        <p>Base currency: {currencyData.base_currency}</p>
      </div>
    </div>
  )
}

export default CurrencyCard 