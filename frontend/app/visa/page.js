'use client';
import { useState } from 'react';

export default function VisaPage() {
  const [country, setCountry] = useState('');
  const [requirements, setRequirements] = useState(null);
  const [loading, setLoading] = useState(false);
  const [files, setFiles] = useState([]);
  const [analysis, setAnalysis] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);

  const fetchRequirements = async () => {
    if (!country.trim()) return;
    setLoading(true);
    setRequirements(null);
    setAnalysis(null);
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/visa/requirements?country=${encodeURIComponent(country)}`);
      const data = await res.json();
      setRequirements(data);
    } catch {
      setRequirements({ error: 'Failed to fetch requirements' });
    }
    setLoading(false);
  };

  const analyzeDocuments = async () => {
    if (!files.length || !country.trim()) return;
    setAnalyzing(true);
    setAnalysis(null);
    try {
      const formData = new FormData();
      formData.append('country', country);
      files.forEach(f => formData.append('files', f));
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/visa/analyze`, {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      setAnalysis(data.analysis);
    } catch {
      setAnalysis({ error: 'Analysis failed. Please try again.' });
    }
    setAnalyzing(false);
  };

  const renderContent = (text) => {
    if (!text) return null;
    const html = text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br/>');
    return <p className="text-sm leading-relaxed text-gray-300" dangerouslySetInnerHTML={{ __html: html }} />;
  };

  return (
    <main className="min-h-screen bg-gray-950 px-4 py-8">
      <div className="max-w-3xl mx-auto">

        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <a href="/" className="text-gray-400 hover:text-white transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
              <path strokeLinecap="round" strokeLinejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
            </svg>
          </a>
          <div>
            <h1 className="text-white font-semibold text-xl">Visa Intelligence</h1>
            <p className="text-gray-500 text-sm">Check requirements + verify your documents</p>
          </div>
        </div>

        {/* Country Input */}
        <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6 mb-6">
          <label className="text-gray-400 text-sm mb-2 block">Where are you travelling?</label>
          <div className="flex gap-3">
            <input
              type="text"
              value={country}
              onChange={e => setCountry(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && fetchRequirements()}
              placeholder="e.g. Japan, Italy, USA, Dubai..."
              className="flex-1 bg-gray-800 text-white border border-gray-700 rounded-xl px-4 py-3 focus:outline-none focus:border-blue-500 transition-colors placeholder-gray-500 text-sm"
            />
            <button
              onClick={fetchRequirements}
              disabled={loading}
              className="bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-xl px-5 py-3 text-sm font-medium transition-colors"
            >
              {loading ? 'Searching...' : 'Check'}
            </button>
          </div>
          <div className="flex flex-wrap gap-2 mt-3">
            {['USA', 'UK', 'Japan', 'Italy', 'Dubai', 'Thailand'].map(c => (
              <button key={c} onClick={() => setCountry(c)}
                className="text-xs text-gray-400 hover:text-white bg-gray-800 hover:bg-gray-700 border border-gray-700 rounded-lg px-3 py-1.5 transition-all">
                {c}
              </button>
            ))}
          </div>
        </div>

        {/* Requirements Result */}
        {requirements && (
          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6 mb-6">
            {requirements.error ? (
              <p className="text-red-400 text-sm">{requirements.error}</p>
            ) : (
              <>
                <div className="flex items-center gap-2 mb-4">
                  <span className="text-blue-400 text-xs font-medium bg-blue-950 border border-blue-800 rounded-lg px-3 py-1">
                    {requirements.normalized_query !== requirements.country
                      ? `Showing Schengen requirements for ${requirements.country}`
                      : requirements.country}
                  </span>
                </div>
                {renderContent(requirements.answer)}
              </>
            )}
          </div>
        )}

        {/* Document Upload */}
        {requirements && !requirements.error && (
          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6 mb-6">
            <h2 className="text-white font-medium mb-1">Check your documents</h2>
            <p className="text-gray-500 text-sm mb-4">Upload your PDFs — we'll tell you what's ready and what's missing</p>

            <div
              className="border-2 border-dashed border-gray-700 rounded-xl p-8 text-center cursor-pointer hover:border-blue-500 transition-colors"
              onClick={() => document.getElementById('file-input').click()}
            >
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-8 h-8 text-gray-500 mx-auto mb-2">
                <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
              </svg>
              <p className="text-gray-400 text-sm">Click to upload PDFs</p>
              <p className="text-gray-600 text-xs mt-1">Passport, bank statements, ITR, employment letter...</p>
              <input
                id="file-input"
                type="file"
                multiple
                accept=".pdf"
                className="hidden"
                onChange={e => setFiles(Array.from(e.target.files))}
              />
            </div>

            {files.length > 0 && (
              <div className="mt-3 space-y-2">
                {files.map((f, i) => (
                  <div key={i} className="flex items-center gap-2 text-sm text-gray-400 bg-gray-800 rounded-lg px-3 py-2">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-4 h-4 text-blue-400">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
                    </svg>
                    {f.name}
                  </div>
                ))}
                <button
                  onClick={analyzeDocuments}
                  disabled={analyzing}
                  className="w-full bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-xl py-3 text-sm font-medium transition-colors mt-2"
                >
                  {analyzing ? 'Analyzing...' : `Analyze ${files.length} document${files.length > 1 ? 's' : ''}`}
                </button>
              </div>
            )}
          </div>
        )}

        {/* Analysis Results */}
        {analysis && (
          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-white font-medium">Document Analysis</h2>
              <span className={`text-xs font-medium rounded-lg px-3 py-1 border ${
                analysis.overall_status === 'ready'
                  ? 'text-green-400 bg-green-950 border-green-800'
                  : analysis.overall_status === 'incomplete'
                  ? 'text-red-400 bg-red-950 border-red-800'
                  : 'text-amber-400 bg-amber-950 border-amber-800'
              }`}>
                {analysis.overall_status === 'ready' ? '✅ Ready' :
                 analysis.overall_status === 'incomplete' ? '❌ Incomplete' : '⚠️ Needs Review'}
              </span>
            </div>

            {analysis.summary && (
              <p className="text-gray-400 text-sm mb-4">{analysis.summary}</p>
            )}

            {analysis.fulfilled?.length > 0 && (
              <div className="mb-4">
                <p className="text-green-400 text-xs font-medium mb-2">✅ FULFILLED</p>
                {analysis.fulfilled.map((item, i) => (
                  <div key={i} className="flex items-start gap-2 text-sm text-gray-300 mb-1">
                    <span className="text-green-400 mt-0.5">✓</span>
                    <span><strong>{item.document}</strong> — {item.detail}</span>
                  </div>
                ))}
              </div>
            )}

            {analysis.missing?.length > 0 && (
              <div className="mb-4">
                <p className="text-red-400 text-xs font-medium mb-2">❌ MISSING</p>
                {analysis.missing.map((item, i) => (
                  <div key={i} className="flex items-start gap-2 text-sm text-gray-300 mb-1">
                    <span className="text-red-400 mt-0.5">✗</span>
                    <span><strong>{item.document}</strong> — {item.detail}</span>
                  </div>
                ))}
              </div>
            )}

            {analysis.warnings?.length > 0 && (
              <div>
                <p className="text-amber-400 text-xs font-medium mb-2">⚠️ WARNINGS</p>
                {analysis.warnings.map((item, i) => (
                  <div key={i} className="flex items-start gap-2 text-sm text-gray-300 mb-1">
                    <span className="text-amber-400 mt-0.5">!</span>
                    <span><strong>{item.document}</strong> — {item.detail}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

      </div>
    </main>
  );
}