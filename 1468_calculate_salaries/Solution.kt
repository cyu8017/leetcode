// LeetCode 1468 - Calculate Salaries
// https://leetcode.com/problems/calculate-salaries/

class Solution {
    companion object {
        const val QUERY = "SELECT company_id, employee_id, employee_name,\n" +
            "       ROUND(salary * CASE\n" +
            "           WHEN MAX(salary) OVER (PARTITION BY company_id) < 1000 THEN 1\n" +
            "           WHEN MAX(salary) OVER (PARTITION BY company_id) <= 10000 THEN 0.76\n" +
            "           ELSE 0.51\n" +
            "       END) AS salary\n" +
            "FROM Salaries"
    }
}
