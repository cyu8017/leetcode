// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

class Solution {
    fun countWays(nums: List<Int>): Int {
        val sorted = nums.sorted()
        val n = sorted.size
        var ans = 0
        if (sorted[0] > 0) ans++
        for (i in 0 until n) {
            val selected = i + 1
            if (selected > sorted[i] && (i == n - 1 || selected < sorted[i + 1])) ans++
        }
        return ans
    }
}
