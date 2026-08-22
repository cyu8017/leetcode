// LeetCode 3150 - Invalid Tweets II
// https://leetcode.com/problems/invalid-tweets-ii/

const char* QUERY =
    "\n"
    "SELECT tweet_id\n"
    "FROM Tweets\n"
    "WHERE LENGTH(content) > 140\n"
    "    OR (LENGTH(content) - LENGTH(REPLACE(content, '@', ''))) > 3\n"
    "    OR (LENGTH(content) - LENGTH(REPLACE(content, '#', ''))) > 3\n"
    "ORDER BY 1;\n";
