// LeetCode 3436 - Find Valid Emails
// https://leetcode.com/problems/find-valid-emails/

class Solution {
    public static final String QUERY = """
SELECT user_id, email
FROM Users
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z][A-Za-z0-9]*\\.com$'
ORDER BY 1;
""";
}
