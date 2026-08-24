// LeetCode 3909 - Compare Sums Of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

class Solution {
    fun compareBitonicSums(nums: IntArray): Int {
        var l = nums[0]
        var r = 0
        for (x in nums) { r += x }
        for (i in 1 until nums.size) {
            if (nums[i - 1] > nums[i]) break
            l += nums[i]
            r -= nums[i - 1]
        }
        if (l == r) return -1
        if (l > r) return 0
        return 1
    }
}
