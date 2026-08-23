// LeetCode 1336 - Number of Transactions per Visit
// https://leetcode.com/problems/number-of-transactions-per-visit/

public class Solution {
    public const string QUERY = @"
WITH RECURSIVE counts AS (
    SELECT 0 AS transactions_count
    UNION ALL
    SELECT transactions_count + 1
    FROM counts
    WHERE transactions_count < (SELECT COUNT(*) FROM Transactions GROUP BY user_id, transaction_date ORDER BY COUNT(*) DESC LIMIT 1)
), per_visit AS (
    SELECT v.user_id, v.visit_date, COUNT(t.amount) AS transactions_count
    FROM Visits v
    LEFT JOIN Transactions t
      ON t.user_id = v.user_id AND t.transaction_date = v.visit_date
    GROUP BY v.user_id, v.visit_date
)
SELECT c.transactions_count, COUNT(p.transactions_count) AS visits_count
FROM counts c
LEFT JOIN per_visit p USING (transactions_count)
GROUP BY c.transactions_count
ORDER BY c.transactions_count
";
}
