// LeetCode 2010 - The Number Of Seniors And Juniors To Join The Company Ii
// https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company-ii/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    s AS (\n" +
            "        SELECT\n" +
            "            employee_id,\n" +
            "            SUM(salary) OVER (ORDER BY salary) AS cur\n" +
            "        FROM Candidates\n" +
            "        WHERE experience = 'Senior'\n" +
            "    ),\n" +
            "    j AS (\n" +
            "        SELECT\n" +
            "            employee_id,\n" +
            "            IFNULL(\n" +
            "                (SELECT\n" +
            "                    MAX(cur)\n" +
            "                FROM s\n" +
            "                WHERE cur <= 70000),\n" +
            "                0\n" +
            "            ) + SUM(salary) OVER (ORDER BY salary) AS cur\n" +
            "        FROM Candidates\n" +
            "        WHERE experience = 'Junior'\n" +
            "    )\n" +
            "SELECT\n" +
            "    employee_id\n" +
            "FROM s\n" +
            "WHERE cur <= 70000\n" +
            "UNION\n" +
            "SELECT\n" +
            "    employee_id\n" +
            "FROM j\n" +
            "WHERE cur <= 70000"
    }
}
