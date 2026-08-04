// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

class Solution {
    fun largestUniqueNumber(nums: IntArray): Int {
        val count = mutableMapOf<Int, Int>()
        for (x in nums) count[x] = count.getOrDefault(x, 0) + 1
        var ans = -1
        for ((value, freq) in count) {
            if (freq == 1) ans = maxOf(ans, value)
        }
        return ans
    }
}
