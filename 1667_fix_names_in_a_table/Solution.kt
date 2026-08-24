// LeetCode 1667 - Fix Names In A Table
// https://leetcode.com/problems/fix-names-in-a-table/

class Solution {
    companion object {
        const val QUERY = "SELECT user_id, CONCAT(UPPER(LEFT(name,1)),LOWER(SUBSTRING(name,2))) name\n" +
            "FROM Users ORDER BY user_id"
    }
}
