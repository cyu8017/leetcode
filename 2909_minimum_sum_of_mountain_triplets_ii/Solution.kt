// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

class Solution {
    fun minimumSum(nums: IntArray): Int {
        var n = nums.size
        var left = IntArray(n)
        var right = IntArray(n)
        var mn = 1  shl  30
        for (i in 0 until n) {
            left[i] = mn
            if (nums[i] < mn) mn = nums[i]
        }
        mn = 1  shl  30
        for (i in n - 1 downTo 0) {
            right[i] = mn
            if (nums[i] < mn) mn = nums[i]
        }
        var ans = 1  shl  30
        for (j in 1 until n - 1) {
            if (left[j] < nums[j] && right[j] < nums[j]) {
                var cand = left[j] + nums[j] + right[j]
                if (cand < ans) ans = cand
            }
        }
        return ans == if ((1  shl  30)) -1 else ans
    }
}
