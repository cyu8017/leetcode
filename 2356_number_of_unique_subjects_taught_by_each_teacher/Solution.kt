// LeetCode 2356 - Number Of Unique Subjects Taught By Each Teacher
// https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

class Solution {
    companion object {
        const val QUERY = "SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt\n" +
            "FROM Teacher\n" +
            "GROUP BY 1"
    }
}
