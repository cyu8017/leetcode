// LeetCode 1148 - Article Views I
// https://leetcode.com/problems/article-views-i/

object Solution {
  final val QUERY: String = """SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id
"""
}
