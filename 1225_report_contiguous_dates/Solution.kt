// LeetCode 1225 - Report Contiguous Dates
// https://leetcode.com/problems/report-contiguous-dates/

class Solution {
    companion object {
        const val QUERY = "WITH dates AS (\n" +
            "    SELECT fail_date AS day, 'failed' AS period_state FROM Failed\n" +
            "    UNION ALL\n" +
            "    SELECT success_date, 'succeeded' FROM Succeeded\n" +
            "), grouped AS (\n" +
            "    SELECT day, period_state,\n" +
            "           DATE_SUB(day, INTERVAL ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY day) DAY) AS grp\n" +
            "    FROM dates\n" +
            "    WHERE day BETWEEN '2019-01-01' AND '2019-12-31'\n" +
            ")\n" +
            "SELECT period_state, MIN(day) AS start_date, MAX(day) AS end_date\n" +
            "FROM grouped\n" +
            "GROUP BY period_state, grp\n" +
            "ORDER BY start_date"
    }
}
