// LeetCode 2978 - Symmetric Coordinates
// https://leetcode.com/problems/symmetric-coordinates/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    P AS (\n" +
            "        SELECT\n" +
            "            ROW_NUMBER() OVER () AS id,\n" +
            "            x,\n" +
            "            y\n" +
            "        FROM Coordinates\n" +
            "    )\n" +
            "SELECT DISTINCT\n" +
            "    p1.x,\n" +
            "    p1.y\n" +
            "FROM\n" +
            "    P AS p1\n" +
            "    JOIN P AS p2 ON p1.x = p2.y AND p1.y = p2.x AND p1.x <= p1.y AND p1.id != p2.id\n" +
            "ORDER BY 1, 2"
    }
}
