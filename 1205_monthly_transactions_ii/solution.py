QUERY = """
WITH activity AS (
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country,
           1 AS approved_count, amount AS approved_amount,
           0 AS chargeback_count, 0 AS chargeback_amount
    FROM Transactions
    WHERE state = 'approved'
    UNION ALL
    SELECT DATE_FORMAT(c.trans_date, '%Y-%m'), t.country,
           0, 0, 1, t.amount
    FROM Chargebacks c
    JOIN Transactions t ON t.id = c.trans_id
)
SELECT month, country,
       SUM(approved_count) AS approved_count,
       SUM(approved_amount) AS approved_amount,
       SUM(chargeback_count) AS chargeback_count,
       SUM(chargeback_amount) AS chargeback_amount
FROM activity
GROUP BY month, country
"""
