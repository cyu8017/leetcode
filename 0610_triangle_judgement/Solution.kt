// LeetCode 0610 - Triangle Judgement
// https://leetcode.com/problems/triangle-judgement/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    x,\n" +
            "    y,\n" +
            "    z,\n" +
            "    CASE\n" +
            "        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'\n" +
            "        ELSE 'No'\n" +
            "    END AS triangle\n" +
            "FROM Triangle"
    }
}
