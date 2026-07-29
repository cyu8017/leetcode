// LeetCode 0610 - Triangle Judgement
// https://leetcode.com/problems/triangle-judgement/

class Solution {
    public static final String QUERY = """
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle
""";
}
