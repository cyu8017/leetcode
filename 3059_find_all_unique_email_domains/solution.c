// LeetCode 3059 - Find All Unique Email Domains
// https://leetcode.com/problems/find-all-unique-email-domains/

const char* QUERY =
    "\n"
    "SELECT SUBSTRING_INDEX(email, '@', -1) AS email_domain, COUNT(1) AS count\n"
    "FROM Emails\n"
    "WHERE email LIKE '%.com'\n"
    "GROUP BY 1\n"
    "ORDER BY 1;\n";
