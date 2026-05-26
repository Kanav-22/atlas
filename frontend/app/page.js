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
    return <p style={{ fontSize: '14px', lineHeight: 1.8, color: '#94a3b8', fontFamily: "'Sora', sans-serif" }} dangerouslySetInnerHTML={{ __html: html }} />;
  };

  const quickCountries = ['USA', 'UK', 'Japan', 'Italy', 'Dubai', 'Thailand', 'Canada', 'Australia'];

  return (
    <main style={{ minHeight: '100vh', background: '#080c14', color: '#f8fafc', fontFamily: "'Sora', sans-serif" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');
        * { box-sizing: border-box; }

        .visa-hero {
          padding: 60px 24px 40px;
          max-width: 700px;
          margin: 0 auto;
          text-align: center;
        }

        .visa-tag {
          display: inline-block;
          padding: 5px 14px;
          border-radius: 9999px;
          border: 1px solid rgba(16, 185, 129, 0.3);
          background: rgba(16, 185, 129, 0.08);
          color: #10b981;
          font-size: 12px;
          font-weight: 500;
          margin-bottom: 20px;
        }

        .visa-title {
          font-size: clamp(32px, 5vw, 52px);
          font-weight: 700;
          letter-spacing: -1.5px;
          line-height: 1.05;
          margin-bottom: 16px;
          color: #f8fafc;
        }

        .visa-sub {
          font-size: 15px;
          color: #475569;
          line-height: 1.6;
          margin-bottom: 40px;
        }

        .search-row {
          display: flex;
          gap: 8px;
          max-width: 560px;
          margin: 0 auto 16px;
        }

        .country-input {
          flex: 1;
          background: rgba(255,255,255,0.04);
          border: 1px solid rgba(255,255,255,0.08);
          border-radius: 12px;
          padding: 14px 18px;
          color: #f8fafc;
          font-size: 14px;
          font-family: 'Sora', sans-serif;
          outline: none;
          transition: border-color 0.2s;
        }

        .country-input::placeholder { color: #334155; }
        .country-input:focus { border-color: rgba(16, 185, 129, 0.4); }

        .check-btn {
          background: #10b981;
          border: none;
          border-radius: 12px;
          padding: 14px 22px;
          color: #080c14;
          font-size: 14px;
          font-weight: 600;
          font-family: 'Sora', sans-serif;
          cursor: pointer;
          transition: background 0.2s;
          white-space: nowrap;
        }

        .check-btn:hover { background: #34d399; }
        .check-btn:disabled { opacity: 0.5; cursor: not-allowed; }

        .country-pills {
          display: flex;
          flex-wrap: wrap;
          gap: 8px;
          justify-content: center;
          max-width: 560px;
          margin: 0 auto;
        }

        .country-pill {
          padding: 6px 14px;
          border-radius: 8px;
          border: 1px solid rgba(255,255,255,0.06);
          background: rgba(255,255,255,0.02);
          color: #475569;
          font-size: 12px;
          font-family: 'Sora', sans-serif;
          cursor: pointer;
          transition: all 0.2s;
        }

        .country-pill:hover { border-color: rgba(16,185,129,0.3); color: #94a3b8; }

        .content-area {
          max-width: 700px;
          margin: 40px auto 0;
          padding: 0 24px 80px;
        }

        .result-card {
          background: rgba(255,255,255,0.02);
          border: 1px solid rgba(255,255,255,0.06);
          border-radius: 16px;
          padding: 28px;
          margin-bottom: 16px;
        }

        .result-label {
          display: inline-block;
          padding: 4px 12px;
          border-radius: 6px;
          background: rgba(16, 185, 129, 0.1);
          border: 1px solid rgba(16, 185, 129, 0.2);
          color: #10b981;
          font-size: 11px;
          font-weight: 600;
          letter-spacing: 0.5px;
          text-transform: uppercase;
          margin-bottom: 16px;
        }

        .upload-zone {
          border: 1px dashed rgba(255,255,255,0.1);
          border-radius: 12px;
          padding: 40px 24px;
          text-align: center;
          cursor: pointer;
          transition: all 0.2s;
        }

        .upload-zone:hover { border-color: rgba(16,185,129,0.3); background: rgba(16,185,129,0.02); }

        .upload-title { font-size: 15px; font-weight: 500; color: #f1f5f9; margin-bottom: 6px; }
        .upload-sub { font-size: 12px; color: #334155; }

        .file-item {
          display: flex;
          align-items: center;
          gap: 10px;
          padding: 10px 14px;
          background: rgba(255,255,255,0.03);
          border: 1px solid rgba(255,255,255,0.06);
          border-radius: 8px;
          margin-top: 8px;
          font-size: 13px;
          color: #94a3b8;
        }

        .analyze-btn {
          width: 100%;
          margin-top: 12px;
          background: rgba(16, 185, 129, 0.1);
          border: 1px solid rgba(16, 185, 129, 0.2);
          border-radius: 10px;
          padding: 14px;
          color: #10b981;
          font-size: 14px;
          font-weight: 600;
          font-family: 'Sora', sans-serif;
          cursor: pointer;
          transition: all 0.2s;
        }

        .analyze-btn:hover { background: rgba(16, 185, 129, 0.15); }
        .analyze-btn:disabled { opacity: 0.4; cursor: not-allowed; }

        .analysis-card {
          background: rgba(255,255,255,0.02);
          border: 1px solid rgba(255,255,255,0.06);
          border-radius: 16px;
          padding: 28px;
        }

        .analysis-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 20px;
        }

        .analysis-title { font-size: 16px; font-weight: 600; color: #f1f5f9; }

        .status-badge {
          padding: 5px 12px;
          border-radius: 6px;
          font-size: 12px;
          font-weight: 600;
        }

        .status-ready { background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.2); color: #10b981; }
        .status-incomplete { background: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.2); color: #ef4444; }
        .status-review { background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.2); color: #f59e0b; }

        .doc-section-label {
          font-size: 11px;
          font-weight: 600;
          letter-spacing: 1px;
          text-transform: uppercase;
          margin-bottom: 10px;
          margin-top: 16px;
        }

        .doc-item {
          display: flex;
          align-items: flex-start;
          gap: 10px;
          padding: 10px 0;
          border-bottom: 1px solid rgba(255,255,255,0.04);
          font-size: 13px;
          color: #94a3b8;
          line-height: 1.5;
        }

        .doc-item:last-child { border-bottom: none; }

        .summary-text {
          font-size: 13px;
          color: #475569;
          line-height: 1.7;
          margin-bottom: 16px;
          padding-bottom: 16px;
          border-bottom: 1px solid rgba(255,255,255,0.04);
        }

        .disclaimer {
          font-size: 11px;
          color: #1e293b;
          text-align: center;
          margin-top: 24px;
          line-height: 1.6;
        }
      `}</style>

      {/* Hero */}
      <div className="visa-hero">
        <div className="visa-tag">🛂 Visa Intelligence</div>
        <h1 className="visa-title">Know exactly what<br />you need to travel</h1>
        <p className="visa-sub">Requirements for Indian passport holders. Upload your documents<br />to see what's ready and what's missing.</p>

        <div className="search-row">
          <input
            type="text"
            className="country-input"
            value={country}
            onChange={e => setCountry(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && fetchRequirements()}
            placeholder="Where are you going? e.g. Japan, Italy, USA..."
          />
          <button className="check-btn" onClick={fetchRequirements} disabled={loading}>
            {loading ? 'Checking...' : 'Check →'}
          </button>
        </div>

        <div className="country-pills">
          {quickCountries.map(c => (
            <button key={c} className="country-pill" onClick={() => setCountry(c)}>{c}</button>
          ))}
        </div>
      </div>

      {/* Content */}
      <div className="content-area">

        {/* Requirements */}
        {requirements && (
          <div className="result-card">
            {requirements.error ? (
              <p style={{ color: '#ef4444', fontSize: '14px' }}>{requirements.error}</p>
            ) : (
              <>
                <div className="result-label">
                  {requirements.normalized_query !== requirements.country
                    ? `Schengen → ${requirements.country}`
                    : requirements.country}
                </div>
                {renderContent(requirements.answer)}
              </>
            )}
          </div>
        )}

        {/* Upload section */}
        {requirements && !requirements.error && (
          <div className="result-card">
            <div style={{ marginBottom: '16px' }}>
              <div style={{ fontSize: '16px', fontWeight: 600, color: '#f1f5f9', marginBottom: '4px' }}>Document checker</div>
              <div style={{ fontSize: '13px', color: '#334155' }}>Upload your PDFs — we'll cross-reference against the requirements</div>
            </div>

            <div className="upload-zone" onClick={() => document.getElementById('visa-file-input').click()}>
              <div style={{ fontSize: '24px', marginBottom: '8px' }}>📄</div>
              <div className="upload-title">Drop PDFs here or click to browse</div>
              <div className="upload-sub">Passport, bank statements, ITR, employment letter, hotel bookings...</div>
              <input id="visa-file-input" type="file" multiple accept=".pdf" style={{ display: 'none' }}
                onChange={e => setFiles(Array.from(e.target.files))} />
            </div>

            {files.length > 0 && (
              <>
                {files.map((f, i) => (
                  <div key={i} className="file-item">
                    <span style={{ color: '#10b981' }}>📎</span> {f.name}
                  </div>
                ))}
                <button className="analyze-btn" onClick={analyzeDocuments} disabled={analyzing}>
                  {analyzing ? 'Analyzing your documents...' : `Analyze ${files.length} document${files.length > 1 ? 's' : ''} →`}
                </button>
              </>
            )}
          </div>
        )}

        {/* Analysis result */}
        {analysis && (
          <div className="analysis-card">
            <div className="analysis-header">
              <div className="analysis-title">Document Analysis</div>
              <div className={`status-badge ${
                analysis.overall_status === 'ready' ? 'status-ready' :
                analysis.overall_status === 'incomplete' ? 'status-incomplete' : 'status-review'
              }`}>
                {analysis.overall_status === 'ready' ? '✓ Ready to apply' :
                 analysis.overall_status === 'incomplete' ? '✗ Incomplete' : '⚠ Needs review'}
              </div>
            </div>

            {analysis.summary && <p className="summary-text">{analysis.summary}</p>}

            {analysis.fulfilled?.length > 0 && (
              <>
                <div className="doc-section-label" style={{ color: '#10b981' }}>✓ Fulfilled</div>
                {analysis.fulfilled.map((item, i) => (
                  <div key={i} className="doc-item">
                    <span style={{ color: '#10b981', marginTop: '1px' }}>✓</span>
                    <span><strong style={{ color: '#f1f5f9' }}>{item.document}</strong> — {item.detail}</span>
                  </div>
                ))}
              </>
            )}

            {analysis.missing?.length > 0 && (
              <>
                <div className="doc-section-label" style={{ color: '#ef4444' }}>✗ Missing</div>
                {analysis.missing.map((item, i) => (
                  <div key={i} className="doc-item">
                    <span style={{ color: '#ef4444', marginTop: '1px' }}>✗</span>
                    <span><strong style={{ color: '#f1f5f9' }}>{item.document}</strong> — {item.detail}</span>
                  </div>
                ))}
              </>
            )}

            {analysis.warnings?.length > 0 && (
              <>
                <div className="doc-section-label" style={{ color: '#f59e0b' }}>⚠ Warnings</div>
                {analysis.warnings.map((item, i) => (
                  <div key={i} className="doc-item">
                    <span style={{ color: '#f59e0b', marginTop: '1px' }}>!</span>
                    <span><strong style={{ color: '#f1f5f9' }}>{item.document}</strong> — {item.detail}</span>
                  </div>
                ))}
              </>
            )}
          </div>
        )}

        <p className="disclaimer">⚠ Visa information is indicative. Always verify with the official embassy website before applying.</p>
      </div>
    </main>
  );
}