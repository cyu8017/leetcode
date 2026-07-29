// LeetCode 0574 - Winning Candidate
// https://leetcode.com/problems/winning-candidate/

class Solution {
    public static final String QUERY = """
SELECT c.name
FROM Candidate c
JOIN Vote v ON c.id = v.candidateId
GROUP BY c.id, c.name
ORDER BY COUNT(*) DESC
LIMIT 1
""";
}
