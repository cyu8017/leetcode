// LeetCode 2298 - Tasks Count in the Weekend
// https://leetcode.com/problems/tasks-count-in-the-weekend/

class Solution {
    public static final String QUERY = """
SELECT
    SUM(WEEKDAY(submit_date) IN (5, 6)) AS weekend_cnt,
    SUM(WEEKDAY(submit_date) NOT IN (5, 6)) AS working_cnt
FROM Tasks
""";
}
