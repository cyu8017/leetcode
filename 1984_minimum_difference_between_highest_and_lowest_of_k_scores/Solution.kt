// LeetCode 1984
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution {
    fun minimumDifference(nums: IntArray, k: Int): Int {
        nums.sort()
        var ans = Int.MAX_VALUE
        for (i in 0..nums.size - k) ans = minOf(ans, nums[i + k - 1] - nums[i])
        return ans
    }
}
