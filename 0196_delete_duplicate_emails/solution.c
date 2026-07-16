// LeetCode 0196 - Delete Duplicate Emails
// https://leetcode.com/problems/delete-duplicate-emails/

const char *QUERY = "\nDELETE p1\nFROM Person p1\nJOIN Person p2\n  ON p1.email = p2.email\n AND p1.id > p2.id\n";
