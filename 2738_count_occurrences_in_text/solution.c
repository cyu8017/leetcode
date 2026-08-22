// LeetCode 2738 - Count Occurrences in Text
// https://leetcode.com/problems/count-occurrences-in-text/

const char* QUERY =
    "\n"
    "SELECT 'bull' AS word, COUNT(*) AS count\n"
    "FROM Files\n"
    "WHERE content LIKE '% bull %'\n"
    "UNION\n"
    "SELECT 'bear' AS word, COUNT(*) AS count\n"
    "FROM Files\n"
    "WHERE content LIKE '% bear %'\n";
