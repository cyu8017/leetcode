// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

class Solution {
    fun maximumSum(nums: List<Int>): Long {
        val n = nums.size
        val groups = HashMap<Int, Long>()
        var ans = 0L
        for (i in 1..n) {
            val sf = squareFree(i)
            val sum = groups.getOrDefault(sf, 0L) + nums[i - 1]
            groups[sf] = sum
            if (sum > ans) ans = sum
        }
        return ans
    }

    private fun squareFree(x0: Int): Int {
        var x = x0
        var res = 1
        var p = 2
        while (p * p <= x) {
            var cnt = 0
            while (x % p == 0) {
                x /= p
                cnt++
            }
            if (cnt % 2 == 1) res *= p
            p++
        }
        if (x > 1) res *= x
        return res
    }
}
