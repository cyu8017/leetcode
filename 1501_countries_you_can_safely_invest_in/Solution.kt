// LeetCode 1501 - Countries You Can Safely Invest In
// https://leetcode.com/problems/countries-you-can-safely-invest-in/

class Solution {
    companion object {
        const val QUERY = "SELECT c.name AS country\n" +
            "FROM Country c\n" +
            "JOIN Person p ON LEFT(p.phone_number, 3) = c.country_code\n" +
            "JOIN (\n" +
            "    SELECT caller_id AS person_id, duration FROM Calls\n" +
            "    UNION ALL\n" +
            "    SELECT callee_id, duration FROM Calls\n" +
            ") x ON x.person_id = p.id\n" +
            "GROUP BY c.name\n" +
            "HAVING AVG(x.duration) > (SELECT AVG(duration) FROM Calls)"
    }
}
