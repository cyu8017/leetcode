// LeetCode 2020 - Number of Accounts That Did Not Stream
// https://leetcode.com/problems/number-of-accounts-that-did-not-stream/

class Solution {
    public static final String QUERY = """
SELECT COUNT(sub.account_id) AS accounts_count
FROM
    Subscriptions AS sub
    LEFT JOIN Streams USING (account_id)
WHERE
    YEAR(start_date) <= 2021
    AND YEAR(end_date) >= 2021
    AND (YEAR(stream_date) != 2021 OR stream_date > end_date)
""";
}
