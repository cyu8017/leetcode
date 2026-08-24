// LeetCode 1613 - Find The Missing Ids
// https://leetcode.com/problems/find-the-missing-ids/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE ids AS (\n" +
            "  SELECT 1 AS ids\n" +
            "  UNION ALL\n" +
            "  SELECT ids + 1 FROM ids WHERE ids < (SELECT MAX(customer_id) FROM Customers)\n" +
            ")\n" +
            "SELECT ids\n" +
            "FROM ids\n" +
            "WHERE ids NOT IN (SELECT customer_id FROM Customers)\n" +
            "ORDER BY ids;"
    }
}
