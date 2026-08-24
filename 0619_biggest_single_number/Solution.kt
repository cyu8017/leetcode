// LeetCode 0619 - Biggest Single Number
// https://leetcode.com/problems/biggest-single-number/

class Solution {
    companion object {
        const val QUERY = "SELECT MAX(num) AS num\n" +
            "FROM (\n" +
            "    SELECT num\n" +
            "    FROM MyNumbers\n" +
            "    GROUP BY num\n" +
            "    HAVING COUNT(*) = 1\n" +
            ") singles"
    }
}
