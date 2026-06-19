import React, { useState } from 'react';
import API from './api';

function ExpenseForm({ onExpenseAdded }) {
  const [title, setTitle] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('Food'); // Default category
  const [description, setDescription] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const newExpense = {
      title,
      amount: parseFloat(amount),
      category,
      description
    };

    try {
      // Send the POST request to your secure Django endpoint
      const response = await API.post('expenses/', newExpense);
      
      // Clear the form fields on success
      setTitle('');
      setAmount('');
      setDescription('');
      
      // Tell the parent component to refresh the expense list
      onExpenseAdded(response.data);
    } catch (err) {
      alert(err.response?.data?.detail || 'Failed to add expense. Check your fields.');
    }
  };

  return (
    <div style={{ backgroundColor: '#f8f9fa', padding: '20px', borderRadius: '8px', marginBottom: '30px', border: '1px solid #e9ecef' }}>
      <h3>➕ Add New Expense</h3>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '10px' }}>
          <label style={{ display: 'block', fontWeight: 'bold' }}>Title:</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }} required />
        </div>
        
        <div style={{ marginBottom: '10px' }}>
          <label style={{ display: 'block', fontWeight: 'bold' }}>Amount ($):</label>
          <input type="number" step="0.01" value={amount} onChange={(e) => setAmount(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }} required />
        </div>

        <div style={{ marginBottom: '10px' }}>
          <label style={{ display: 'block', fontWeight: 'bold' }}>Category:</label>
          <select value={category} onChange={(e) => setCategory(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}>
            <option value="Food">Food</option>
            <option value="Travel">Travel</option>
            <option value="Rent">Rent</option>
            <option value="Utilities">Utilities</option>
            <option value="Entertainment">Entertainment</option>
          </select>
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', fontWeight: 'bold' }}>Description:</label>
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc', height: '60px' }} />
        </div>

        <button type="submit" style={{ backgroundColor: '#28a745', color: 'white', padding: '10px 15px', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}>
          Save Expense
        </button>
      </form>
    </div>
  );
}

export default ExpenseForm;