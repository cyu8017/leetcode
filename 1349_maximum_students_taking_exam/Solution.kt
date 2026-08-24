// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

class Solution {
    fun maxStudents(seats: Array<CharArray>): Int {
        val rows = seats.size
        val cols = seats[0].size
        val validRows = Array(rows) { ArrayList<Int>() }
        for (r in 0 until rows) {
            var available = 0
            for (c in 0 until cols) {
                if (seats[r][c] == '.') available = available or (1 shl c)
            }
            for (mask in 0 until (1 shl cols)) {
                if (mask and available.inv() == 0 && mask and (mask shl 1) == 0) {
                    validRows[r].add(mask)
                }
            }
        }
        var dp = HashMap<Int, Int>()
        dp[0] = 0
        for (masks in validRows) {
            val nxt = HashMap<Int, Int>()
            for (mask in masks) {
                for ((previous, count) in dp) {
                    if (mask and (previous shl 1) == 0 && mask and (previous ushr 1) == 0) {
                        nxt[mask] = maxOf(nxt.getOrDefault(mask, 0), count + Integer.bitCount(mask))
                    }
                }
            }
            dp = nxt
        }
        return dp.values.maxOrNull() ?: 0
    }
}
