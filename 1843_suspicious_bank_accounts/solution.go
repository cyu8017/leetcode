// LeetCode 1843 - Suspicious Bank Accounts
// https://leetcode.com/problems/suspicious-bank-accounts/

const QUERY = `
WITH MonthlyIncome AS (
    SELECT
        account_id,
        DATE_FORMAT(day, '%Y-%m') AS month,
        SUM(amount) AS income
    FROM Transactions
    WHERE type = 'Creditor'
    GROUP BY account_id, DATE_FORMAT(day, '%Y-%m')
),
Exceeds AS (
    SELECT
        mi.account_id,
        mi.month,
        CASE WHEN mi.income > a.max_income THEN 1 ELSE 0 END AS exceeded
    FROM MonthlyIncome mi
    JOIN Accounts a ON mi.account_id = a.account_id
),
WithPrev AS (
    SELECT
        account_id,
        exceeded,
        LAG(exceeded) OVER (
            PARTITION BY account_id
            ORDER BY month
        ) AS prev_exceeded
    FROM Exceeds
)
SELECT DISTINCT account_id
FROM WithPrev
WHERE exceeded = 1 AND prev_exceeded = 1
`
