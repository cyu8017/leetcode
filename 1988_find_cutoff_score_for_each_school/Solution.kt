// LeetCode 1988 - Find Cutoff Score For Each School
// https://leetcode.com/problems/find-cutoff-score-for-each-school/

class Solution {
    companion object {
        const val QUERY = "SELECT school_id, MIN(IFNULL(score, -1)) AS score\n" +
            "FROM Schools AS s\n" +
            "LEFT JOIN Exam AS e ON s.capacity >= e.student_count\n" +
            "GROUP BY school_id"
    }
}
