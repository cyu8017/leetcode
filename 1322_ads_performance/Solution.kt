// LeetCode 1322 - Ads Performance
// https://leetcode.com/problems/ads-performance/

class Solution {
    companion object {
        const val QUERY = "SELECT ad_id,\n" +
            "       ROUND(IFNULL(100 * SUM(action = 'Clicked') /\n" +
            "                    NULLIF(SUM(action IN ('Clicked', 'Viewed')), 0), 0), 2) AS ctr\n" +
            "FROM Ads\n" +
            "GROUP BY ad_id\n" +
            "ORDER BY ctr DESC, ad_id"
    }
}
