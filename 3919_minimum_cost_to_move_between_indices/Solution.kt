// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

class Solution {
    fun minCost(nums: IntArray, queries: Array<IntArray>): IntArray {
        var n = nums.size
        var s1 = IntArray(n)
        var s2 = IntArray(n)
        for (i in 1 until n) {
            var c1 = 1
            if (i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]) c1 = nums[i] - nums[i - 1]
            var c2 = 1
            if (i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i]) c2 = nums[i] - nums[i - 1]
            s1[i] = s1[i - 1] + c1
            s2[i] = s2[i - 1] + c2
        }
        var ans = IntArray(queries.size)
        for (i in 0 until queries.size) {
            var l = queries[i][0]
            var r = queries[i][1]
            ans[i] =if ((l < r)) (s1[r] - s1[l]) else (s2[l] - s2[r])
        }
        return ans
    }
}
