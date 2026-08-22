// LeetCode 3436 - Find Valid Emails
// https://leetcode.com/problems/find-valid-emails/

const char* QUERY =
    "\n"
    "SELECT user_id, email\n"
    "FROM Users\n"
    "WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z][A-Za-z0-9]*\\\\.com$'\n"
    "ORDER BY 1;\n";
