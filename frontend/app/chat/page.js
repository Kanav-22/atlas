'use client';
import { useState, useEffect, useRef } from 'react';
import { useSearchParams } from 'next/navigation';

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const searchParams = useSearchParams();
  const bottomRef = useRef(null);
  const hasSentInitial = useRef(false);

  useEffect(() => {
    const q = searchParams.get('q');
    if (q && !hasSentInitial.current) {
      hasSentInitial.current = true;
      sendMessage(q);
    }
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async (text) => {
    const userMsg = text || input;
    if (!userMsg.trim()) return;

    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setInput('');
    setLoading(true);

    try {
      const history = messages.map(m => ({ role: m.role, content: m.content }));
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMsg, history })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (err) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Something went wrong. Please try again.' }]);
    }
    setLoading(false);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    sendMessage();
  };

  const renderContent = (content) => {
    const html = content
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n/g, '<br/>');
    return <p className="text-sm leading-relaxed" dangerouslySetInnerHTML={{ __html: html }} />;
  };

  return (
    <main className="min-h-screen bg-gray-950 flex flex-col">
      <div className="border-b border-gray-800 px-6 py-4 flex items-center gap-3">
        <a href="/" className="text-gray-400 hover:text-white transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
            <path strokeLinecap="round" strokeLinejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
          </svg>
        </a>
        <h1 className="text-white font-semibold text-lg">Atlas</h1>
        <span className="text-gray-500 text-sm">AI Travel Assistant</span>
      </div>

      <div className="flex-1 overflow-y-auto px-4 py-6 max-w-3xl w-full mx-auto">
        {messages.length === 0 && (
          <div className="text-center text-gray-500 mt-20">
            <p className="text-lg">Ask me anything about travel</p>
            <p className="text-sm mt-2">Flights, hotels, weather, trip planning</p>
          </div>
        )}

        {messages.map((msg, i) => (
          <div key={i} className={`mb-6 flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            {msg.role === 'assistant' && (
              <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white text-xs font-bold mr-3 mt-1 shrink-0">
                A
              </div>
            )}
            <div className={`max-w-2xl rounded-2xl px-5 py-4 ${
              msg.role === 'user'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-900 text-gray-100 border border-gray-800'
            }`}>
              {renderContent(msg.content)}
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex justify-start mb-6">
            <div className="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white text-xs font-bold mr-3 shrink-0">
              A
            </div>
            <div className="bg-gray-900 border border-gray-800 rounded-2xl px-5 py-4">
              <div className="flex gap-1">
                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{animationDelay: '0ms'}}></div>
                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{animationDelay: '150ms'}}></div>
                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{animationDelay: '300ms'}}></div>
              </div>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="border-t border-gray-800 px-4 py-4">
        <form onSubmit={handleSubmit} className="max-w-3xl mx-auto relative">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about flights, hotels, weather..."
            className="w-full bg-gray-900 text-white border border-gray-700 rounded-2xl px-6 py-4 pr-16 focus:outline-none focus:border-blue-500 transition-colors placeholder-gray-500"
            disabled={loading}
          />
          <button
            type="submit"
            disabled={loading}
            className="absolute right-4 top-1/2 -translate-y-1/2 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-xl p-2.5 transition-colors"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
              <path strokeLinecap="round" strokeLinejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
            </svg>
          </button>
        </form>
      </div>
    </main>
  );
}