import React, { useState } from 'react';
import { useRewards } from '../hooks/useRewards';
import './RewardsDashboard.css';

/**
 * RewardsDashboard Component
 * 
 * Main interface for the loyalty system.
 * Allows users to view balance, register purchases, and redeem points.
 */
const RewardsDashboard: React.FC = () => {
    const { balance, loading, feedback, addPoints, redeem } = useRewards();
    const [purchaseAmount, setPurchaseAmount] = useState<string>('');

    const handlePurchaseSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const amount = parseFloat(purchaseAmount);
        if (!isNaN(amount) && amount > 0) {
            await addPoints(amount);
            setPurchaseAmount('');
        }
    };

    const handleRedeemClick = async () => {
        // Standard redemption of 10 points
        await redeem(10);
    };

    return (
        <div className="dashboard-container">
            <header className="header">
                <h1>Loyalty Rewards</h1>
                <p>Accumulate points and get incredible benefits.</p>
            </header>

            <section className="hero-card">
                <span className="label">Your Balance</span>
                <span className="points">{loading && balance === 0 ? '...' : balance}</span>
                <span className="label">Points</span>
            </section>

            <div className="sections-grid">
                {/* Register Purchase Section */}
                <section className="card">
                    <h2>🛒 Register Purchase</h2>
                    <form onSubmit={handlePurchaseSubmit} className="input-group">
                        <input
                            type="number"
                            placeholder="Amount ($)"
                            value={purchaseAmount}
                            onChange={(e) => setPurchaseAmount(e.target.value)}
                            min="1"
                            step="any"
                            disabled={loading}
                            required
                        />
                        <button type="submit" disabled={loading || !purchaseAmount}>
                            {loading ? 'Processing...' : 'Add Points'}
                        </button>
                    </form>
                    <p style={{ fontSize: '0.8rem', color: '#718096', marginTop: '1rem' }}>
                        Earn 1 point for every $1,000 spent.
                    </p>
                </section>

                {/* Redeem Points Section */}
                <section className="card">
                    <h2>🎁 Redeem Points</h2>
                    <div className="input-group">
                        <p>Redeem 10 points for special discounts!</p>
                        <button
                            onClick={handleRedeemClick}
                            disabled={loading || balance < 10}
                            className={balance < 10 ? 'btn-secondary' : ''}
                        >
                            {loading ? 'Processing...' : 'Redeem 10 Pts'}
                        </button>
                        <p style={{ fontSize: '0.8rem', color: '#718096', marginTop: '1rem' }}>
                            Minimum points required: 10
                        </p>
                    </div>
                </section>
            </div>

            {/* Feedback Area */}
            <div className="feedback-area">
                {feedback && (
                    <div className={`alert ${feedback.type}`}>
                        {feedback.type === 'success' ? '✅' : '❌'} {feedback.message}
                    </div>
                )}
            </div>
        </div>
    );
};

export default RewardsDashboard;
