# Postman Usage Guide: Loyalty Rewards API

This guide provides the necessary details to test the rewards system endpoints using Postman.

## 🧰 Prerequisites
- **Base URL**: `http://localhost:8000/api/rewards`
- **Headers**: 
  - `Content-Type: application/json`

---

## 1. Get Reward Balance
Retrieves the current point balance and transaction history.

- **Method**: `GET`
- **URL**: `{{BaseURL}}/balance/`
- **Body**: None
- **Response Example (200 OK)**:
```json
{
    "username": "admin",
    "total_points": 50,
    "updated_at": "2026-02-12T11:20:00Z",
    "transactions": [
        {
            "id": 1,
            "transaction_type": "EARNED",
            "transaction_type_display": "Earned",
            "points": 50,
            "amount": "50000.00",
            "created_at": "2026-02-12T11:20:00Z"
        }
    ]
}
```

---

## 2. Register Purchase (Earn Points)
Adds points to the user's balance based on a purchase amount ($1,000 = 1 pt).

- **Method**: `POST`
- **URL**: `{{BaseURL}}/purchase/`
- **Body (JSON)**:
```json
{
    "amount": 50000.00
}
```
- **Response Example (201 Created)**:
```json
{
    "message": "Points added successfully.",
    "new_balance": 50,
    "amount_processed": 50000.0
}
```

---

## 3. Redeem Points
Redeems a specific number of points for monetary value (1 pt = $100).

- **Method**: `POST`
- **URL**: `{{BaseURL}}/redeem/`
- **Body (JSON)**:
```json
{
    "points": 10
}
```
- **Response Example (200 OK)**:
```json
{
    "message": "Points redeemed successfully.",
    "new_balance": 40,
    "points_redeemed": 10
}
```

---
> [!NOTE]
> If you attempt to redeem more points than available, the system will return a `400 Bad Request` with a descriptive error code: `insufficient_points`.
