// LeetCode 1741 - Find Total Time Spent by Each Employee
// https://leetcode.com/problems/find-total-time-spent-by-each-employee/

public class Solution {
    public static final String QUERY = "SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time\n" +
        "FROM Employees\n" +
        "GROUP BY event_day, emp_id;\n" +
        "";
}
