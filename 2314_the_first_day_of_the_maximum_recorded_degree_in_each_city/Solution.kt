// LeetCode 2314 - The First Day Of The Maximum Recorded Degree In Each City
// https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            *,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY city_id\n" +
            "                ORDER BY degree DESC, day\n" +
            "            ) AS rk\n" +
            "        FROM Weather\n" +
            "    )\n" +
            "SELECT city_id, day, degree\n" +
            "FROM T\n" +
            "WHERE rk = 1\n" +
            "ORDER BY 1"
    }
}
