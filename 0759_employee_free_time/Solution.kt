// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

class Solution {
    fun employeeFreeTime(schedule: Array<Array<IntArray>>): Array<IntArray> {
        val intervals = ArrayList<IntArray>()
        for (employee in schedule) {
            for (item in employee) intervals.add(intArrayOf(item[0], item[1]))
        }
        intervals.sortBy { it[0] }
        val merged = ArrayList<IntArray>()
        for (iv in intervals) {
            if (merged.isEmpty() || merged[merged.size - 1][1] < iv[0]) merged.add(iv)
            else merged[merged.size - 1][1] = maxOf(merged[merged.size - 1][1], iv[1])
        }
        val result = ArrayList<IntArray>()
        for (i in 1 until merged.size) {
            result.add(intArrayOf(merged[i - 1][1], merged[i][0]))
        }
        return result.toTypedArray()
    }
}
