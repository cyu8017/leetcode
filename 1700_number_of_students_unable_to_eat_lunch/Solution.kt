// LeetCode 1700 - Number Of Students Unable To Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution {
    fun countStudents(students: IntArray, sandwiches: IntArray): Int {
        val c = IntArray(2)
        for (x in students) c[x]++
        for (i in sandwiches.indices) {
            val x = sandwiches[i]
            if (c[x] == 0) return students.size - i
            c[x]--
        }
        return 0
    }
}
