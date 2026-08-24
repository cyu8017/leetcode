// LeetCode 1907 - Count Salary Categories
// https://leetcode.com/problems/count-salary-categories/

class Solution {
    companion object {
        const val QUERY = "SELECT 'Low Salary' AS category,\n" +
            "       SUM(income < 20000) AS accounts_count\n" +
            "FROM Accounts\n" +
            "UNION ALL\n" +
            "SELECT 'Average Salary' AS category,\n" +
            "       SUM(income BETWEEN 20000 AND 50000) AS accounts_count\n" +
            "FROM Accounts\n" +
            "UNION ALL\n" +
            "SELECT 'High Salary' AS category,\n" +
            "       SUM(income > 50000) AS accounts_count\n" +
            "FROM Accounts"
    }
}
