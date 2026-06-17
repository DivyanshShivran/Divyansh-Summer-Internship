import React, { useEffect, useState } from 'react';
import API from './api';
import Login from './Login';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('access_token'));
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!isAuthenticated) return;

    // Fetch secure data now that we are authenticated
    // Note: Change 'expenses/' to match whatever endpoint you created in Django week 1!
    API.get('expenses/') 
      .then((response) => {
        setData(response.data);
      })
      .catch((err) => {
        setError(err.response?.data?.detail || 'Failed to fetch data');
      });
  }, [isAuthenticated]);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setIsAuthenticated(false);
    setData([]);
  };

  // If the user isn't logged in, display the Login Component
  if (!isAuthenticated) {
    return <Login onLoginSuccess={() => setIsAuthenticated(true)} />;
  }

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif', maxWidth: '600px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2>Expense Tracker Workspace</h2>
        <button onClick={handleLogout} style={{ padding: '8px 12px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
          Logout
        </button>
      </div>
      <hr />
      
      {error ? (
        <div style={{ padding: '15px', backgroundColor: '#ffeef0', color: '#e02424', borderRadius: '6px' }}>
          <strong>Error:</strong> {error}
        </div>
      ) : (
        <div>
          <h3>Your Records:</h3>
          {data.length === 0 ? <p>No data records returned from API yet.</p> : (
            <ul>
              {data.map(item => <li key={item.id}>{item.title || item.description} - ${item.amount}</li>)}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default App;