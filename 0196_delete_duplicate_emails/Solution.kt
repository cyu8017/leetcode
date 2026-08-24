// LeetCode 0196 - Delete Duplicate Emails
// https://leetcode.com/problems/delete-duplicate-emails/

class Solution {
    companion object {
        const val QUERY = "DELETE p1\n" +
            "FROM Person p1\n" +
            "JOIN Person p2\n" +
            "  ON p1.email = p2.email\n" +
            " AND p1.id > p2.id"
    }
}
