// LeetCode 1204 - Last Person To Fit In The Bus
// https://leetcode.com/problems/last-person-to-fit-in-the-bus/

class Solution {
    companion object {
        const val QUERY = "SELECT person_name\n" +
            "FROM (\n" +
            "    SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) AS total_weight\n" +
            "    FROM Queue\n" +
            ") q\n" +
            "WHERE total_weight <= 1000\n" +
            "ORDER BY turn DESC\n" +
            "LIMIT 1"
    }
}
