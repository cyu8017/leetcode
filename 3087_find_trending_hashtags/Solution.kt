// LeetCode 3087 - Find Trending Hashtags
// https://leetcode.com/problems/find-trending-hashtags/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    CONCAT('#', SUBSTRING_INDEX(SUBSTRING_INDEX(tweet, '#', -1), ' ', 1)) AS hashtag,\n" +
            "    COUNT(1) AS hashtag_count\n" +
            "FROM Tweets\n" +
            "WHERE DATE_FORMAT(tweet_date, '%Y%m') = '202402'\n" +
            "GROUP BY 1\n" +
            "ORDER BY 2 DESC, 1 DESC\n" +
            "LIMIT 3;"
    }
}
