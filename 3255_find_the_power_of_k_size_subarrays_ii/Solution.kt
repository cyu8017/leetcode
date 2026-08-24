// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution {
    fun resultsArray(nums: IntArray, k: Int): IntArray {
        var n = nums.size
        var ans = IntArray(n - k + 1)
        if (k == 1) return nums
        var streak = 1
        for (i in 1 until n) {
            if (nums[i] == nums[i - 1] + 1) streak++
            else streak = 1
            if (i >= k - 1) ans[i - k + 1] = streak >=if (k) nums[i] else -1
        }
        return ans
    }
}
