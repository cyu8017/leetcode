// LeetCode 1462 - Course Schedule IV
// https://leetcode.com/problems/course-schedule-iv/

class Solution {
    fun checkIfPrerequisite(
        numCourses: Int,
        prerequisites: Array<IntArray>,
        queries: Array<IntArray>
    ): List<Boolean> {
        val reach = Array(numCourses) { BooleanArray(numCourses) }
        for (edge in prerequisites) reach[edge[0]][edge[1]] = true
        for (k in 0 until numCourses) {
            for (i in 0 until numCourses) {
                if (reach[i][k]) {
                    for (j in 0 until numCourses) {
                        reach[i][j] = reach[i][j] || reach[k][j]
                    }
                }
            }
        }
        return queries.map { reach[it[0]][it[1]] }
    }
}
