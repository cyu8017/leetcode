// LeetCode 1501 - Countries You Can Safely Invest In
// https://leetcode.com/problems/countries-you-can-safely-invest-in/

class Solution {
    public static final String QUERY = """
SELECT c.name AS country
FROM Country c
JOIN Person p ON LEFT(p.phone_number, 3) = c.country_code
JOIN (
    SELECT caller_id AS person_id, duration FROM Calls
    UNION ALL
    SELECT callee_id, duration FROM Calls
) x ON x.person_id = p.id
GROUP BY c.name
HAVING AVG(x.duration) > (SELECT AVG(duration) FROM Calls)
""";
}
