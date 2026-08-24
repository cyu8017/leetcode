// LeetCode 0585 - Investments In 2016
// https://leetcode.com/problems/investments-in-2016/

class Solution {
    companion object {
        const val QUERY = "SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016\n" +
            "FROM Insurance\n" +
            "WHERE tiv_2015 IN (\n" +
            "    SELECT tiv_2015\n" +
            "    FROM Insurance\n" +
            "    GROUP BY tiv_2015\n" +
            "    HAVING COUNT(*) > 1\n" +
            ")\n" +
            "AND (lat, lon) IN (\n" +
            "    SELECT lat, lon\n" +
            "    FROM Insurance\n" +
            "    GROUP BY lat, lon\n" +
            "    HAVING COUNT(*) = 1\n" +
            ")"
    }
}
