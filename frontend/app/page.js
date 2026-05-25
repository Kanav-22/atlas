'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const [query, setQuery] = useState('');
  const router = useRouter();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    router.push(`/chat?q=${encodeURIComponent(query)}`);
  };

  const examples = [
    "Find flights from Delhi to Mumbai on 2026-06-15",
    "Hotels in Goa from June 20 to June 25",
    "What's the weather like in Manali?",
    "Plan a trip from Bangalore to Jaipur next weekend"
  ];

  return (
    <main className="min-h-screen bg-gray-950 flex flex-col items-center justify-center px-4">
      <div className="w-full max-w-2xl">
        {/* Logo */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white mb-3">
            Atlas
          </h1>
          <p className="text-gray-400 text-lg">
            Your AI travel intelligence assistant
          </p>
        </div>

        {/* Search Bar */}
        <form onSubmit={handleSubmit} className="relative">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask anything about travel..."
            className="w-full bg-gray-900 text-white border border-gray-700 rounded-2xl px-6 py-5 pr-16 text-lg focus:outline-none focus:border-blue-500 transition-colors placeholder-gray-500"
          />
          <button
            type="submit"
            className="absolute right-4 top-1/2 -translate-y-1/2 bg-blue-600 hover:bg-blue-700 text-white rounded-xl p-3 transition-colors"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
              <path strokeLinecap="round" strokeLinejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
            </svg>
          </button>
        </form>

        {/* Example queries */}
        <div className="mt-8">
          <p className="text-gray-500 text-sm mb-4 text-center">Try asking</p>
          <div className="grid grid-cols-1 gap-2">
            {examples.map((example, i) => (
              <button
                key={i}
                onClick={() => setQuery(example)}
                className="text-left text-gray-400 hover:text-white bg-gray-900 hover:bg-gray-800 border border-gray-800 hover:border-gray-600 rounded-xl px-4 py-3 text-sm transition-all"
              >
                {example}
              </button>
            ))}
          </div>
        </div>
      </div>
    </main>
  );
}