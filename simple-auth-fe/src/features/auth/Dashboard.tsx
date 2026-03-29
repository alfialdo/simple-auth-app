import React from 'react';
import { useAuth } from '../../core/AuthContext';

export const Dashboard = () => {
  const { user, logout } = useAuth();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', backgroundColor: '#f3f4f6', fontFamily: 'system-ui, sans-serif' }}>
      <h1 style={{ fontSize: '4rem', fontWeight: 'bold', color: '#1f2937', marginBottom: '2rem', textAlign: 'center' }}>
        Welcome, {user}
      </h1>
      <button 
        onClick={logout}
        style={{ padding: '0.75rem 2rem', fontSize: '1.125rem', fontWeight: '600', backgroundColor: '#ef4444', color: 'white', border: 'none', borderRadius: '0.5rem', cursor: 'pointer', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)' }}
      >
        Sign Out
      </button>
    </div>
  );
};
