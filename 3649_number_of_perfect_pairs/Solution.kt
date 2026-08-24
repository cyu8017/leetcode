// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

class Solution {
    fun perfectPairs(nums: IntArray): Long {
        var n = nums.size
        var absNums = IntArray(n)
        for (i in 0 until n) { absNums[i] = kotlin.math.abs(nums[i]) }
        absNums.sort()
        var ans = 0
        var j = 0
        for (i in 0 until n) {
            if (j < i + 1) j = i + 1
            while (j < n && absNums[j] <= 2 * absNums[i]) j++
            ans += j - i - 1
        }
        return ans
    }
}
