// LeetCode 1148 - Article Views I
// https://leetcode.com/problems/article-views-i/

const char* QUERY =
    "\n"
    "SELECT DISTINCT author_id AS id\n"
    "FROM Views\n"
    "WHERE author_id = viewer_id\n"
    "ORDER BY id\n";
