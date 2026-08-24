// LeetCode 0197 - Rising Temperature
// https://leetcode.com/problems/rising-temperature/

class Solution {
    companion object {
        const val QUERY = "SELECT w1.id\n" +
            "FROM Weather w1\n" +
            "JOIN Weather w2\n" +
            "  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1\n" +
            "WHERE w1.temperature > w2.temperature"
    }
}
