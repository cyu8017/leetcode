// LeetCode 1308 - Running Total For Different Genders
// https://leetcode.com/problems/running-total-for-different-genders/

class Solution {
    companion object {
        const val QUERY = "SELECT gender, day,\n" +
            "       SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total\n" +
            "FROM Scores\n" +
            "ORDER BY gender, day"
    }
}
