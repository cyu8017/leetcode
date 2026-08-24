// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution {
    fun sortTheStudents(score: Array<IntArray>, k: Int): Array<IntArray> {
        score.sortByDescending { it[k] }
        return score
    }
}
