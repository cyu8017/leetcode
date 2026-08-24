// LeetCode 1421 - Npv Queries
// https://leetcode.com/problems/npv-queries/

class Solution {
    companion object {
        const val QUERY = "SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv\n" +
            "FROM Queries q\n" +
            "LEFT JOIN NPV n ON n.id = q.id AND n.year = q.year"
    }
}
