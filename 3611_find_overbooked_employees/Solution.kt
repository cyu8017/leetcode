// LeetCode 3611 - Find Overbooked Employees
// https://leetcode.com/problems/find-overbooked-employees/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    week_meeting_hours AS (\n" +
            "        SELECT\n" +
            "            employee_id,\n" +
            "            YEAR(meeting_date) AS year,\n" +
            "            WEEK(meeting_date, 1) AS week,\n" +
            "            SUM(duration_hours) hours\n" +
            "        FROM meetings\n" +
            "        GROUP BY 1, 2, 3\n" +
            "    ),\n" +
            "    intensive_weeks AS (\n" +
            "        SELECT\n" +
            "            employee_id,\n" +
            "            employee_name,\n" +
            "            department,\n" +
            "            count(1) AS meeting_heavy_weeks\n" +
            "        FROM\n" +
            "            week_meeting_hours\n" +
            "            JOIN employees USING (employee_id)\n" +
            "        WHERE hours >= 20\n" +
            "        GROUP BY 1\n" +
            "    )\n" +
            "SELECT employee_id, employee_name, department, meeting_heavy_weeks\n" +
            "FROM intensive_weeks\n" +
            "WHERE meeting_heavy_weeks >= 2\n" +
            "ORDER BY 4 DESC, 2;"
    }
}
