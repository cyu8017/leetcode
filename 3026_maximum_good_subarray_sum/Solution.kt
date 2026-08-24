// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

class Solution {
    fun maximumSubarraySum(nums: IntArray, k: Int): Long {
        var p = HashMap<Int, Long>()
        p[nums[0]] = 0L
        var s = 0
        var n = nums.size
        var ans = Long.MIN_VALUE
        for (i in 0 until n) {
            s += nums[i]
            if (p.containsKey(nums[i] - k)) ans = maxOf(ans, s - p[nums[i] - k])
            if (p.containsKey(nums[i] + k)) ans = maxOf(ans, s - p[nums[i] + k])
            if (i + 1 == n) break
            var old = p[nums[i + 1]]
            if (old == null || s < old) p[nums[i + 1]] = s
        }
        return ans ==if (Long.MIN_VALUE) 0 else ans
    }
}
