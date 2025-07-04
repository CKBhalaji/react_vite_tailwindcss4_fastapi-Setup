import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [helloMessage, setHelloMessage] = useState('');
  const [dbStatus, setDbStatus] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchApiData = async () => {
      try {
        // Fetch from /api/hello (Vite will proxy this to http://localhost:8000/hello)
        const helloResponse = await axios.get('/api/hello');
        setHelloMessage(helloResponse.data.message);
        // console.log(helloResponse.data.message);

        // Fetch from /api/database-status (Vite will proxy this to http://localhost:8000/database-status)
        const dbResponse = await axios.get('/api/database-status');
        setDbStatus(dbResponse.data.status);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Failed to connect to backend API or database.');
        if (err.response) {
            console.error("Response data:", err.response.data);
            console.error("Response status:", err.response.status);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchApiData();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <header className="bg-gradient-to-r from-blue-500 to-indigo-600 text-white p-6 rounded-lg shadow-xl mb-8 w-full max-w-2xl text-center">
        <h1 className="text-4xl font-extrabold mb-2">
          React + Vite + Tailwind + FastAPI
        </h1>
        <p className="text-lg">A Full-Stack Starter Kit</p>
      </header>

      <section className="bg-white p-6 rounded-lg shadow-lg w-full max-w-2xl text-center">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Backend API Status</h2>
        {loading ? (
          <p className="text-gray-600">Loading...</p>
        ) : error ? (
          <p className="text-red-500 font-semibold">{error}</p>
        ) : (
          <div>
            <p className="text-gray-700 mb-2">
              **Hello Message from FastAPI:** <span className="font-semibold text-blue-600">"{helloMessage}"</span>
            </p>
            <p className="text-gray-700">
              **Database Status:** <span className="font-semibold text-green-600">"{dbStatus}"</span>
            </p>
          </div>
        )}
      </section>

      <footer className="mt-8 text-gray-600 text-sm">
        <p>&copy; {new Date().getFullYear()} Full-Stack AI Starter. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;