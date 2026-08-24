// LeetCode 3051 - Find Candidates For Data Scientist Position
// https://leetcode.com/problems/find-candidates-for-data-scientist-position/

class Solution {
    companion object {
        const val QUERY = "SELECT candidate_id\n" +
            "FROM Candidates\n" +
            "WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')\n" +
            "GROUP BY 1\n" +
            "HAVING COUNT(1) = 3\n" +
            "ORDER BY 1;"
    }
}
