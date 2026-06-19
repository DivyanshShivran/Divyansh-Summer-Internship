import React, { useEffect, useState } from 'react';
import API from './api';
import Login from './Login';
import ExpenseForm from './ExpenseForm';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('access_token'));
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!isAuthenticated) return;

    // Fetch existing expenses from Django backend
    API.get('expenses/') 
      .then((response) => {
        setData(response.data);
      })
      .catch((err) => {
        setError(err.response?.data?.detail || 'Failed to fetch data');
      });
  }, [isAuthenticated]);

  // Callback to append newly created expenses directly into the UI state array
  const handleExpenseAdded = (newExpense) => {
    setData((prevData) => [newExpense, ...prevData]);
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setIsAuthenticated(false);
    setData([]);
  };

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
      <hr style={{ marginBottom: '20px' }} />
      
      {/* Mount the interactive form here */}
      <ExpenseForm onExpenseAdded={handleExpenseAdded} />

      {error ? (
        <div style={{ padding: '15px', backgroundColor: '#ffeef0', color: '#e02424', borderRadius: '6px' }}>
          <strong>Error:</strong> {error}
        </div>
      ) : (
        <div>
          <h3>Your Expense History:</h3>
          {data.length === 0 ? <p>No data records returned from API yet.</p> : (
            <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
              {data.map(item => (
                <li key={item.id} style={{ padding: '12px', borderBottom: '1px solid #eee', display: 'flex', justifyContent: 'space-between', backgroundColor: '#fff' }}>
                  <div>
                    <strong>{item.title}</strong> <span style={{ fontSize: '12px', color: '#666', marginLeft: '10px' }}>({item.category})</span>
                    <p style={{ margin: '4px 0 0 0', fontSize: '13px', color: '#888' }}>{item.description}</p>
                  </div>
                  <span style={{ fontWeight: 'bold', color: '#dc3545' }}>-${item.amount}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default App;