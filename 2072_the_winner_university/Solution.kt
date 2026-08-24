// LeetCode 2072 - The Winner University
// https://leetcode.com/problems/the-winner-university/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    CASE\n" +
            "        WHEN n1.cnt > n2.cnt THEN 'New York University'\n" +
            "        WHEN n1.cnt < n2.cnt THEN 'California University'\n" +
            "        ELSE 'No Winner'\n" +
            "    END AS winner\n" +
            "FROM\n" +
            "    (SELECT COUNT(1) AS cnt FROM NewYork WHERE score >= 90) AS n1,\n" +
            "    (SELECT COUNT(1) AS cnt FROM California WHERE score >= 90) AS n2"
    }
}
