// LeetCode 1149 - Article Views Ii
// https://leetcode.com/problems/article-views-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT viewer_id AS id\n" +
            "FROM Views\n" +
            "GROUP BY viewer_id, view_date\n" +
            "HAVING COUNT(DISTINCT article_id) > 1\n" +
            "ORDER BY id"
    }
}
