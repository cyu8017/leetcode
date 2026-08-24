// LeetCode 3150 - Invalid Tweets II
// https:// leetcode.com/problems/invalid-tweets-ii/

object Solution {
  final val QUERY: String = """SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 140
    OR (LENGTH(content) - LENGTH(REPLACE(content, '@', ''))) > 3
    OR (LENGTH(content) - LENGTH(REPLACE(content, '#', ''))) > 3
ORDER BY 1;
"""
}
