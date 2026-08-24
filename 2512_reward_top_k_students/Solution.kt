// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

class Solution {
    fun topStudents(
        positive_feedback: Array<String>,
        negative_feedback: Array<String>,
        report: Array<String>,
        student_id: IntArray,
        k: Int
    ): IntArray {
        val pos = positive_feedback.toHashSet()
        val neg = negative_feedback.toHashSet()
        val arr = Array(report.size) { IntArray(2) }
        for (i in report.indices) {
            var score = 0
            for (w in report[i].split(" ")) {
                if (w.isEmpty()) continue
                when {
                    w in pos -> score += 3
                    w in neg -> score--
                }
            }
            arr[i][0] = student_id[i]
            arr[i][1] = score
        }
        arr.sortWith(compareByDescending<IntArray> { it[1] }.thenBy { it[0] })
        return IntArray(k) { arr[it][0] }
    }
}
