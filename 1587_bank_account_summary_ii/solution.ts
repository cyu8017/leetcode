// LeetCode 1587 - Bank Account Summary Ii
// https://leetcode.com/problems/bank-account-summary-ii/

export const QUERY = `SELECT u.name, SUM(t.amount) AS balance
FROM Users u JOIN Transactions t ON t.account = u.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000\n`;
