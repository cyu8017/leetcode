// LeetCode 3061 - Calculate Trapping Rain Water
// https://leetcode.com/problems/calculate-trapping-rain-water/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            *,\n" +
            "            MAX(height) OVER (ORDER BY id) AS l,\n" +
            "            MAX(height) OVER (ORDER BY id DESC) AS r\n" +
            "        FROM Heights\n" +
            "    )\n" +
            "SELECT SUM(LEAST(l, r) - height) AS total_trapped_water\n" +
            "FROM T;"
    }
}
