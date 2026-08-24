// LeetCode 2989 - Class Performance
// https://leetcode.com/problems/class-performance/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    MAX(assignment1 + assignment2 + assignment3) - MIN(\n" +
            "        assignment1 + assignment2 + assignment3\n" +
            "    ) AS difference_in_score\n" +
            "FROM Scores"
    }
}
