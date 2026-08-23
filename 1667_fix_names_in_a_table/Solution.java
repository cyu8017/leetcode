// LeetCode 1667 - Fix Names in a Table
// https://leetcode.com/problems/fix-names-in-a-table/

class Solution {
    public static final String QUERY = """
SELECT user_id, CONCAT(UPPER(LEFT(name,1)),LOWER(SUBSTRING(name,2))) name
FROM Users ORDER BY user_id
""";
}
