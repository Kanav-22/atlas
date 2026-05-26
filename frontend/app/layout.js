import { Sora } from 'next/font/google';
import './globals.css';
import Navbar from '../components/Navbar';

const sora = Sora({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700'],
  variable: '--font-sora'
});

export const metadata = {
  title: 'Atlas — AI Travel Intelligence',
  description: 'Your AI travel assistant for flights, hotels, weather and visa requirements',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={sora.variable} style={{ margin: 0, background: '#080c14', fontFamily: "'Sora', sans-serif" }}>
        <Navbar />
        {children}
      </body>
    </html>
  );
}