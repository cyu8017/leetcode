// LeetCode 3436 - Find Valid Emails
// https://leetcode.com/problems/find-valid-emails/

class Solution {
    companion object {
        const val QUERY = "SELECT user_id, email\n" +
            "FROM Users\n" +
            "WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z][A-Za-z0-9]*\\\\.com$'\n" +
            "ORDER BY 1;"
    }
}
