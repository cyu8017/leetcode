// LeetCode 2228 - Users With Two Purchases Within Seven Days
// https://leetcode.com/problems/users-with-two-purchases-within-seven-days/

export const QUERY = `WITH
    t AS (
        SELECT
            user_id,
            DATEDIFF(
                purchase_date,
                LAG(purchase_date, 1) OVER (
                    PARTITION BY user_id
                    ORDER BY purchase_date
                )
            ) AS d
        FROM Purchases
    )
SELECT DISTINCT user_id
FROM t
WHERE d <= 7
ORDER BY user_id`;
