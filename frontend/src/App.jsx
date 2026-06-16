import React, { useEffect, useState } from 'react';
import API from './api';

function App() {
  const [notes, setNotes] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Attempt to fetch secure notes data from Django
    API.get('notes/')
      .then((response) => {
        setNotes(response.data);
      })
      .catch((err) => {
        // Since we don't have a login form yet, we expect a 401 error here!
        setError(err.response?.data?.detail || 'Failed to fetch data');
      });
  }, []);

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif', maxWidth: '600px', margin: '0 auto' }}>
      <h2>Expense Tracker Client Workspace</h2>
      <hr />
      
      {error ? (
        <div style={{ padding: '15px', backgroundColor: '#ffeef0', color: '#e02424', borderRadius: '6px', border: '1px solid #fdbbbf' }}>
          <strong>Backend Security Notice:</strong> {error}
        </div>
      ) : (
        <div>
          <h3>Your Notes:</h3>
          {notes.length === 0 ? <p>No records found.</p> : (
            <ul>
              {notes.map(note => <li key={note.id}>{note.title}</li>)}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default App;