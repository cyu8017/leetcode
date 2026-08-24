// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution {
    fun resultsArray(nums: IntArray, k: Int): IntArray {
        var n = nums.size
        var ans = IntArray(n - k + 1)
        for (i in 0 ..n - k) {
            var ok = true
            for (j in i + 1 until i + k) {
                if (nums[j] != nums[j - 1] + 1) { ok = false; break; }
            }
            ans[i] =if (ok) nums[i + k - 1] else -1
        }
        return ans
    }
}
