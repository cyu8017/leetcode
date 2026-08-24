// LeetCode 1843 - Suspicious Bank Accounts
// https://leetcode.com/problems/suspicious-bank-accounts/

class Solution {
    companion object {
        const val QUERY = "WITH MonthlyIncome AS (\n" +
            "    SELECT\n" +
            "        account_id,\n" +
            "        DATE_FORMAT(day, '%Y-%m') AS month,\n" +
            "        SUM(amount) AS income\n" +
            "    FROM Transactions\n" +
            "    WHERE type = 'Creditor'\n" +
            "    GROUP BY account_id, DATE_FORMAT(day, '%Y-%m')\n" +
            "),\n" +
            "Exceeds AS (\n" +
            "    SELECT\n" +
            "        mi.account_id,\n" +
            "        mi.month,\n" +
            "        CASE WHEN mi.income > a.max_income THEN 1 ELSE 0 END AS exceeded\n" +
            "    FROM MonthlyIncome mi\n" +
            "    JOIN Accounts a ON mi.account_id = a.account_id\n" +
            "),\n" +
            "WithPrev AS (\n" +
            "    SELECT\n" +
            "        account_id,\n" +
            "        exceeded,\n" +
            "        LAG(exceeded) OVER (\n" +
            "            PARTITION BY account_id\n" +
            "            ORDER BY month\n" +
            "        ) AS prev_exceeded\n" +
            "    FROM Exceeds\n" +
            ")\n" +
            "SELECT DISTINCT account_id\n" +
            "FROM WithPrev\n" +
            "WHERE exceeded = 1 AND prev_exceeded = 1"
    }
}
