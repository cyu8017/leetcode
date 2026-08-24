// LeetCode 3055 - Top Percentile Fraud
// https://leetcode.com/problems/top-percentile-fraud/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            *,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY state\n" +
            "                ORDER BY fraud_score DESC\n" +
            "            ) AS rk\n" +
            "        FROM Fraud\n" +
            "    )\n" +
            "SELECT policy_id, state, fraud_score\n" +
            "FROM T\n" +
            "WHERE rk = 1\n" +
            "ORDER BY 2, 3 DESC, 1;"
    }
}
