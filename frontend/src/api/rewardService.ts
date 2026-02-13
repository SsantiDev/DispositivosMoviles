import axios from 'axios';
import type { AxiosInstance } from 'axios';
import type { Reward } from '../types/rewards';

/**
 * Configure Axios instance for Reward API.
 * Update baseURL according to your environment.
 */
const api: AxiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api/rewards',
    headers: {
        'Content-Type': 'application/json',
    },
});

/**
 * Interface for the response data after adding points or redeeming.
 * Matches the backend response structure.
 */
interface RewardOperationResponse {
    message: string;
    new_balance: number;
    amount_processed?: number;
    points_redeemed?: number;
}

/**
 * Service to handle Reward-related API calls.
 */
export const rewardService = {
    /**
     * Fetch the current reward balance and history for the authenticated user.
     */
    async fetchBalance(): Promise<Reward> {
        const response = await api.get<Reward>('/balance/');
        return response.data;
    },

    /**
     * Record a new purchase to obtain points.
     * @param amount The total purchase amount.
     */
    async recordPurchase(amount: number): Promise<RewardOperationResponse> {
        const response = await api.post<RewardOperationResponse>('/purchase/', { amount });
        return response.data;
    },

    /**
     * Redeem a specific amount of points.
     * @param points The number of points to redeem.
     */
    async redeemPoints(points: number): Promise<RewardOperationResponse> {
        const response = await api.post<RewardOperationResponse>('/redeem/', { points });
        return response.data;
    },
};

export default api;
