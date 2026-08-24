// LeetCode 2026 - Low Quality Problems
// https://leetcode.com/problems/low-quality-problems/

class Solution {
    companion object {
        const val QUERY = "SELECT problem_id\n" +
            "FROM Problems\n" +
            "WHERE likes / (likes + dislikes) < 0.6\n" +
            "ORDER BY problem_id"
    }
}
