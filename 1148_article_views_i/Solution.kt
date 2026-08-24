// LeetCode 1148 - Article Views I
// https://leetcode.com/problems/article-views-i/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT author_id AS id\n" +
            "FROM Views\n" +
            "WHERE author_id = viewer_id\n" +
            "ORDER BY id"
    }
}
