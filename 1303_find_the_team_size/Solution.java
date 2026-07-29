// LeetCode 1303 - Find The Team Size
// https://leetcode.com/problems/find-the-team-size/

class Solution {
    public static final String QUERY = """
SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size
FROM Employee
""";
}
