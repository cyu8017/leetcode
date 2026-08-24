// LeetCode 2372 - Calculate The Influence Of Each Salesperson
// https://leetcode.com/problems/calculate-the-influence-of-each-salesperson/

class Solution {
    companion object {
        const val QUERY = "SELECT sp.salesperson_id, sp.name, IFNULL(SUM(s.price), 0) AS total\n" +
            "FROM Salesperson AS sp\n" +
            "LEFT JOIN Customer AS c ON sp.salesperson_id = c.salesperson_id\n" +
            "LEFT JOIN Sales AS s ON s.customer_id = c.customer_id\n" +
            "GROUP BY sp.salesperson_id, sp.name"
    }
}
