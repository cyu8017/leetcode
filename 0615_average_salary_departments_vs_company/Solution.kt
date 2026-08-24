// LeetCode 0615 - Average Salary Departments Vs Company
// https://leetcode.com/problems/average-salary-departments-vs-company/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month,\n" +
            "    e.department_id,\n" +
            "    CASE\n" +
            "        WHEN AVG(s.amount) > company.avg_amount THEN 'higher'\n" +
            "        WHEN AVG(s.amount) < company.avg_amount THEN 'lower'\n" +
            "        ELSE 'same'\n" +
            "    END AS comparison\n" +
            "FROM Salary s\n" +
            "JOIN Employee e ON s.employee_id = e.employee_id\n" +
            "JOIN (\n" +
            "    SELECT DATE_FORMAT(pay_date, '%Y-%m') AS pay_month, AVG(amount) AS avg_amount\n" +
            "    FROM Salary\n" +
            "    GROUP BY DATE_FORMAT(pay_date, '%Y-%m')\n" +
            ") company ON DATE_FORMAT(s.pay_date, '%Y-%m') = company.pay_month\n" +
            "GROUP BY DATE_FORMAT(s.pay_date, '%Y-%m'), e.department_id, company.avg_amount"
    }
}
