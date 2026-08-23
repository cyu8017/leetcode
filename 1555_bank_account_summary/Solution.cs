// LeetCode 1555 - Bank Account Summary
// https://leetcode.com/problems/bank-account-summary/

public class Solution {
    public const string QUERY = @"
SELECT u.user_id, u.user_name,
       u.credit + COALESCE(SUM(CASE WHEN t.paid_to = u.user_id THEN t.amount
                                   WHEN t.paid_by = u.user_id THEN -t.amount ELSE 0 END), 0) AS credit,
       CASE WHEN u.credit + COALESCE(SUM(CASE WHEN t.paid_to = u.user_id THEN t.amount
                                             WHEN t.paid_by = u.user_id THEN -t.amount ELSE 0 END), 0) < 0
            THEN 'Yes' ELSE 'No' END AS credit_limit_breached
FROM Users u LEFT JOIN Transactions t
  ON u.user_id IN (t.paid_by, t.paid_to)
GROUP BY u.user_id, u.user_name, u.credit\n
";
}
