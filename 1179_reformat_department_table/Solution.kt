// LeetCode 1179 - Reformat Department Table
// https://leetcode.com/problems/reformat-department-table/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    id,\n" +
            "    SUM(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Apr' THEN revenue END) AS Apr_Revenue,\n" +
            "    SUM(CASE WHEN month = 'May' THEN revenue END) AS May_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Jun' THEN revenue END) AS Jun_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Jul' THEN revenue END) AS Jul_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Aug' THEN revenue END) AS Aug_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Sep' THEN revenue END) AS Sep_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Oct' THEN revenue END) AS Oct_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Nov' THEN revenue END) AS Nov_Revenue,\n" +
            "    SUM(CASE WHEN month = 'Dec' THEN revenue END) AS Dec_Revenue\n" +
            "FROM Department\n" +
            "GROUP BY id"
    }
}
