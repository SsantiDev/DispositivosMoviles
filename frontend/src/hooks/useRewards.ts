import { useState, useCallback, useEffect } from 'react';
import axios from 'axios';
import { rewardService } from '../api/rewardService';
import type { Reward, APIError } from '../types/rewards';

/**
 * Interface for feedback notifications.
 */
export interface Feedback {
    message: string;
    type: 'success' | 'error';
}

/**
 * Custom hook to manage reward balance and transactions.
 * Provides state for balance, loading status, and user feedback.
 */
export const useRewards = () => {
    const [balance, setBalance] = useState<number>(0);
    const [loading, setLoading] = useState<boolean>(false);
    const [feedback, setFeedback] = useState<Feedback | null>(null);

    /**
     * Internal error handler to parse API errors.
     */
    const handleError = useCallback((err: unknown) => {
        if (axios.isAxiosError(err) && err.response?.data) {
            const apiError = err.response.data as APIError;
            setFeedback({
                message: apiError.error || 'API Error occurred',
                type: 'error',
            });
        } else {
            setFeedback({
                message: 'An unexpected connection error occurred.',
                type: 'error',
            });
        }
    }, []);

    /**
     * Fetches the current balance from the backend.
     */
    const loadBalance = useCallback(async () => {
        setLoading(true);
        try {
            const data: Reward = await rewardService.fetchBalance();
            setBalance(data.totalPoints);
        } catch (err) {
            handleError(err);
        } finally {
            setLoading(false);
        }
    }, [handleError]);

    /**
     * Records a purchase and refreshes the balance.
     * @param amount The purchase amount.
     */
    const addPoints = async (amount: number) => {
        setLoading(true);
        setFeedback(null);
        try {
            const response = await rewardService.recordPurchase(amount);
            setFeedback({ message: response.message, type: 'success' });
            await loadBalance(); // Automatic refresh
        } catch (err) {
            handleError(err);
        } finally {
            setLoading(false);
        }
    };

    /**
     * Redeems points and refreshes the balance.
     * @param points The number of points to redeem.
     */
    const redeem = async (points: number) => {
        setLoading(true);
        setFeedback(null);
        try {
            const response = await rewardService.redeemPoints(points);
            setFeedback({ message: response.message, type: 'success' });
            await loadBalance(); // Automatic refresh
        } catch (err) {
            handleError(err);
        } finally {
            setLoading(false);
        }
    };

    // Initial load
    useEffect(() => {
        loadBalance();
    }, [loadBalance]);

    return {
        balance,
        loading,
        feedback,
        loadBalance,
        addPoints,
        redeem,
    };
};
