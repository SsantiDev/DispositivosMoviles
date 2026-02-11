/**
 * Supported transaction types for the rewards system.
 */
export type TransactionType = 'EARNED' | 'REDEEMED';

/**
 * Represents a historical reward transaction record.
 */
export interface RewardTransaction {
    id: number;
    transaction_type: TransactionType;
    transaction_type_display?: string;
    points: number;
    amount: number;
    created_at: string;
}

/**
 * Represents the current state of a user's reward balance.
 */
export interface Reward {
    username?: string;
    total_points: number;
    updated_at: string;
    transactions?: RewardTransaction[];
}

/**
 * Standardized structure for API error responses.
 */
export interface APIError {
    error: string;
    code: string;
}
