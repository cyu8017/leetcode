// LeetCode 3338 - Second Highest Salary Ii
// https://leetcode.com/problems/second-highest-salary-ii/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            emp_id,\n" +
            "            dept,\n" +
            "            DENSE_RANK() OVER (\n" +
            "                PARTITION BY dept\n" +
            "                ORDER BY salary DESC\n" +
            "            ) rk\n" +
            "        FROM Employees\n" +
            "    )\n" +
            "SELECT emp_id, dept\n" +
            "FROM T\n" +
            "WHERE rk = 2\n" +
            "ORDER BY 1;"
    }
}
