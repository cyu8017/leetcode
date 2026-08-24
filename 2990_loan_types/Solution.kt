// LeetCode 2990 - Loan Types
// https://leetcode.com/problems/loan-types/

class Solution {
    companion object {
        const val QUERY = "SELECT user_id\n" +
            "FROM Loans\n" +
            "GROUP BY 1\n" +
            "HAVING SUM(loan_type = 'Refinance') > 0 AND SUM(loan_type = 'Mortgage') > 0\n" +
            "ORDER BY 1"
    }
}
