// LeetCode 2752 - Customers With Maximum Number Of Transactions On Consecutive Days
// https://leetcode.com/problems/customers-with-maximum-number-of-transactions-on-consecutive-days/

var QUERY = `WITH
    s AS (
        SELECT
            customer_id,
            DATE_SUB(
                transaction_date,
                INTERVAL ROW_NUMBER() OVER (
                    PARTITION BY customer_id
                    ORDER BY transaction_date
                ) DAY
            ) AS transaction_date
        FROM Transactions
    ),
    t AS (
        SELECT customer_id, transaction_date, COUNT(1) AS cnt
        FROM s
        GROUP BY 1, 2
    )
SELECT customer_id
FROM t
WHERE cnt = (SELECT MAX(cnt) FROM t)
ORDER BY customer_id`;

module.exports = { QUERY };
