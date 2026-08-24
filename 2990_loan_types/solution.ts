// LeetCode 2990 - Loan Types
// https://leetcode.com/problems/loan-types/

export const QUERY = `SELECT user_id
FROM Loans
GROUP BY 1
HAVING SUM(loan_type = 'Refinance') > 0 AND SUM(loan_type = 'Mortgage') > 0
ORDER BY 1`;
