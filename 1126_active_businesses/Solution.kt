// LeetCode 1126 - Active Businesses
// https://leetcode.com/problems/active-businesses/

class Solution {
    companion object {
        const val QUERY = "WITH avg_occ AS (\n" +
            "    SELECT event_type, AVG(occurrences) AS avg_occ\n" +
            "    FROM Events\n" +
            "    GROUP BY event_type\n" +
            ")\n" +
            "SELECT DISTINCT e.business_id\n" +
            "FROM Events e\n" +
            "JOIN avg_occ a ON e.event_type = a.event_type\n" +
            "GROUP BY e.business_id\n" +
            "HAVING SUM(e.occurrences > a.avg_occ) > 1"
    }
}
