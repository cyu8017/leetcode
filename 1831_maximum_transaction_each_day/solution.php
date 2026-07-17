// LeetCode 1831 - Maximum Transaction Each Day
// https://leetcode.com/problems/maximum-transaction-each-day/

const QUERY = <<<'SQL'
SELECT transaction_id
FROM Transactions t
WHERE amount = (
    SELECT MAX(amount)
    FROM Transactions
    WHERE DATE(day) = DATE(t.day)
)
ORDER BY transaction_id
SQL;
