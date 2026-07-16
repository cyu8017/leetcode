// LeetCode 0182 - Duplicate Emails
// https://leetcode.com/problems/duplicate-emails/

const char* QUERY =
    "\n"
    "SELECT email AS Email\n"
    "FROM Person\n"
    "GROUP BY email\n"
    "HAVING COUNT(*) > 1\n";