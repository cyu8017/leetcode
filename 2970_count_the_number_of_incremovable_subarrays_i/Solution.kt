// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

class Solution {
    fun incremovableSubarrayCount(nums: IntArray): Int {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            for (j in i until n) {
                var prev = -1
                var ok = true
                for (t in 0 until n) {
                    if (t >= i && t <= j) continue
                    if (nums[t] <= prev) {
                        ok = false
                        break
                    }
                    prev = nums[t]
                }
                if (ok) ans++
            }
        }
        return ans
    }
}
