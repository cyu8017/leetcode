// LeetCode 0608 - Tree Node
// https://leetcode.com/problems/tree-node/

class Solution {
    public static final String QUERY = """
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
""";
}
