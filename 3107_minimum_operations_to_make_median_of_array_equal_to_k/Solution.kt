// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

class Solution {
    fun minOperationsToMakeMedianK(nums: IntArray, k: Int): Long {
        nums.sort()
        var n = nums.size
        var m = n  shr  1
        var ans = kotlin.math.abs(nums[m] - k)
        if (nums[m] > k) {
            run {
                var i = m - 1
                while (i >= 0 && nums[i] > k) {
                    ans += nums[i] - k
                    i--
                }
            }
        } else {
            for (i in m + 1 until n && nums[i] < k) { ans += k - nums[i] }
        }
        return ans
    }
}
