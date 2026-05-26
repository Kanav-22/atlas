'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Navbar() {
  const pathname = usePathname();

  return (
    <nav style={{
      position: 'sticky', top: 0, zIndex: 50,
      background: 'rgba(8, 12, 20, 0.85)',
      backdropFilter: 'blur(12px)',
      borderBottom: '1px solid rgba(14, 165, 233, 0.1)',
      padding: '0 24px',
      height: '60px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between'
    }}>
      {/* Logo */}
      <Link href="/" style={{ textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" fill="#0ea5e9"/>
        </svg>
        <span style={{ color: '#f8fafc', fontFamily: "'Sora', sans-serif", fontWeight: 600, fontSize: '18px', letterSpacing: '-0.3px' }}>
          Atlas
        </span>
      </Link>

      {/* Nav Links */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
        <Link href="/chat" style={{
          textDecoration: 'none',
          padding: '8px 16px',
          borderRadius: '8px',
          fontSize: '14px',
          fontFamily: "'Sora', sans-serif",
          fontWeight: 500,
          color: pathname === '/chat' ? '#0ea5e9' : '#94a3b8',
          background: pathname === '/chat' ? 'rgba(14, 165, 233, 0.1)' : 'transparent',
          transition: 'all 0.2s'
        }}>
          Chat
        </Link>
        <Link href="/visa" style={{
          textDecoration: 'none',
          padding: '8px 16px',
          borderRadius: '8px',
          fontSize: '14px',
          fontFamily: "'Sora', sans-serif",
          fontWeight: 500,
          color: pathname === '/visa' ? '#0ea5e9' : '#94a3b8',
          background: pathname === '/visa' ? 'rgba(14, 165, 233, 0.1)' : 'transparent',
          transition: 'all 0.2s'
        }}>
          Visa
        </Link>
        <Link href="/chat" style={{
          textDecoration: 'none',
          padding: '8px 20px',
          borderRadius: '8px',
          fontSize: '14px',
          fontFamily: "'Sora', sans-serif",
          fontWeight: 600,
          color: '#080c14',
          background: '#0ea5e9',
          marginLeft: '8px',
          transition: 'all 0.2s'
        }}>
          Ask Atlas →
        </Link>
      </div>
    </nav>
  );
}