/**
 * Supported transaction types for the rewards system.
 */
export type TransactionType = 'EARNED' | 'REDEEMED';

/**
 * Represents a historical reward transaction record.
 */
export interface RewardTransaction {
    id: number;
    transactionType: TransactionType;
    transactionTypeDisplay?: string;
    points: number;
    amountMoney: number;
    timestamp: string; // ISO format
}

/**
 * Represents the current state of a user's reward balance.
 */
export interface Reward {
    userId: number;
    username?: string;
    totalPoints: number;
    createdAt: string;
    updatedAt: string;
    transactions?: RewardTransaction[];
}

/**
 * Standardized structure for API error responses.
 */
export interface APIError {
    error: string;
    code: string;
}
