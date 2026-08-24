// LeetCode 2020 - Number Of Accounts That Did Not Stream
// https://leetcode.com/problems/number-of-accounts-that-did-not-stream/

class Solution {
    companion object {
        const val QUERY = "SELECT COUNT(sub.account_id) AS accounts_count\n" +
            "FROM\n" +
            "    Subscriptions AS sub\n" +
            "    LEFT JOIN Streams USING (account_id)\n" +
            "WHERE\n" +
            "    YEAR(start_date) <= 2021\n" +
            "    AND YEAR(end_date) >= 2021\n" +
            "    AND (YEAR(stream_date) != 2021 OR stream_date > end_date)"
    }
}
