// LeetCode 0182 - Duplicate Emails
// https://leetcode.com/problems/duplicate-emails/

var QUERY = `
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1
`;