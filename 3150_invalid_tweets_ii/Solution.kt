// LeetCode 3150 - Invalid Tweets Ii
// https://leetcode.com/problems/invalid-tweets-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT tweet_id\n" +
            "FROM Tweets\n" +
            "WHERE LENGTH(content) > 140\n" +
            "    OR (LENGTH(content) - LENGTH(REPLACE(content, '@', ''))) > 3\n" +
            "    OR (LENGTH(content) - LENGTH(REPLACE(content, '#', ''))) > 3\n" +
            "ORDER BY 1;"
    }
}
