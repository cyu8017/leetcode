// LeetCode 2298 - Tasks Count In The Weekend
// https://leetcode.com/problems/tasks-count-in-the-weekend/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    SUM(WEEKDAY(submit_date) IN (5, 6)) AS weekend_cnt,\n" +
            "    SUM(WEEKDAY(submit_date) NOT IN (5, 6)) AS working_cnt\n" +
            "FROM Tasks"
    }
}
