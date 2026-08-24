// LeetCode 3103 - Find Trending Hashtags Ii
// https://leetcode.com/problems/find-trending-hashtags-ii/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE\n" +
            "    FebruaryTweets AS (\n" +
            "        SELECT *\n" +
            "        FROM Tweets\n" +
            "        WHERE YEAR(tweet_date) = 2024 AND MONTH(tweet_date) = 2\n" +
            "    ),\n" +
            "    HashtagToTweet AS (\n" +
            "        SELECT\n" +
            "            REGEXP_SUBSTR(tweet, '#[^\\\\s]+') AS hashtag,\n" +
            "            REGEXP_REPLACE(tweet, '#[^\\\\s]+', '', 1, 1) AS tweet\n" +
            "        FROM FebruaryTweets\n" +
            "        UNION ALL\n" +
            "        SELECT\n" +
            "            REGEXP_SUBSTR(tweet, '#[^\\\\s]+') AS hashtag,\n" +
            "            REGEXP_REPLACE(tweet, '#[^\\\\s]+', '', 1, 1) AS tweet\n" +
            "        FROM HashtagToTweet\n" +
            "        WHERE POSITION('#' IN tweet) > 0\n" +
            "    )\n" +
            "SELECT\n" +
            "    hashtag,\n" +
            "    COUNT(*) AS count\n" +
            "FROM HashtagToTweet\n" +
            "GROUP BY hashtag\n" +
            "ORDER BY count DESC, hashtag DESC\n" +
            "LIMIT 3;"
    }
}
