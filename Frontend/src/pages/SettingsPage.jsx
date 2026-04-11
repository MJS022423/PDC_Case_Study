import React, { useEffect, useState } from 'react';
import { balanceApi } from '../services/api';

export default function SettingsPage() {
  const [balance, setBalance] = useState(0);
  const [addAmount, setAddAmount] = useState('');
  const [subtractAmount, setSubtractAmount] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchBalance();
  }, []);

  const fetchBalance = async () => {
    try {
      const data = await balanceApi.getBalance();
      setBalance(data.balance);
      setError(null);
    } catch (err) {
      console.error('Error fetching balance:', err);
      setError('Failed to fetch balance');
    } finally {
      setLoading(false);
    }
  };

  const handleAddFunds = async () => {
    const amount = parseFloat(addAmount);
    if (isNaN(amount) || amount <= 0) {
      setError('Please enter a valid positive amount');
      return;
    }

    try {
      const result = await balanceApi.addBalance(amount);
      if (result.success) {
        setBalance(result.new_balance);
        setAddAmount('');
        setError(null);
      } else {
        setError(result.message);
      }
    } catch (err) {
      console.error('Error adding funds:', err);
      setError('Failed to add funds');
    }
  };

  const handleSubtractFunds = async () => {
    const amount = parseFloat(subtractAmount);
    if (isNaN(amount) || amount <= 0) {
      setError('Please enter a valid positive amount');
      return;
    }

    if (amount > balance) {
      setError('Cannot subtract more than current balance');
      return;
    }

    try {
      const result = await balanceApi.subtractBalance(amount);
      if (result.success) {
        setBalance(result.new_balance);
        setSubtractAmount('');
        setError(null);
      } else {
        setError(result.message);
      }
    } catch (err) {
      console.error('Error subtracting funds:', err);
      setError('Failed to subtract funds');
    }
  };

  if (loading) {
    return <div className="p-6 text-white">Loading...</div>;
  }

  return (
    <div className="max-w-xl mx-auto p-6">
      <h1 className="text-3xl font-bold text-white mb-8 text-center">⚙️ Settings</h1>

      <div className="bg-slate-800 text-white rounded-xl shadow-lg p-6">
        <h2 className="text-xl font-semibold mb-4">💰 Account Balance</h2>

        <div className="mb-6">
          <p className="text-lg text-gray-300 mb-2">Current Balance</p>
          <p className="text-3xl font-bold text-green-400">
            ${balance.toFixed(2)}
          </p>
        </div>

        <div className="space-y-4">
          {/* Add Funds */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Add Funds
            </label>
            <div className="flex gap-2">
              <input
                type="number"
                value={addAmount}
                onChange={(e) => setAddAmount(e.target.value)}
                placeholder="Enter amount"
                className="flex-1 px-3 py-2 bg-gray-700 text-white rounded-lg focus:outline-none focus:border-green-500"
                min="0"
                step="0.01"
              />
              <button
                onClick={handleAddFunds}
                className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
              >
                Add
              </button>
            </div>
          </div>

          {/* Subtract Funds */}
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Subtract Funds
            </label>
            <div className="flex gap-2">
              <input
                type="number"
                value={subtractAmount}
                onChange={(e) => setSubtractAmount(e.target.value)}
                placeholder="Enter amount"
                className="flex-1 px-3 py-2 bg-gray-700 text-white rounded-lg focus:outline-none focus:border-red-500"
                min="0"
                step="0.01"
              />
              <button
                onClick={handleSubtractFunds}
                className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
              >
                Subtract
              </button>
            </div>
          </div>
        </div>

        {error && (
          <div className="mt-4 text-red-400 bg-red-900 p-3 rounded-lg">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}