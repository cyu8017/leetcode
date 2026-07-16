// LeetCode 0182 - Duplicate Emails
// https://leetcode.com/problems/duplicate-emails/

const char* QUERY = R"SQL(
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1
)SQL";