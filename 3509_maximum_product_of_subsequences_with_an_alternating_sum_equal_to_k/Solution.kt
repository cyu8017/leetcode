// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

class Solution {
    companion object { const val MIN = -5000 }
    lateinit var memo: HashMap<String, Int>
    lateinit var nums: IntArray
    var limit = 0

    fun dp(i: Int, product: Int, state: Int, kk: Int): Int {
        if (i == nums.size) {
            if (kk == 0 && state != 0 && product <= limit) return product
            return MIN
        }
        val key = "$i,$product,$state,$kk"
        memo[key]?.let { return it }
        var res = dp(i + 1, product, state, kk)
        if (state == 0) res = maxOf(res, dp(i + 1, nums[i], 1, kk - nums[i]))
        if (state == 1) {
            var np = product * nums[i]
            if (np > limit + 1) np = limit + 1
            res = maxOf(res, dp(i + 1, np, 2, kk + nums[i]))
        }
        if (state == 2) {
            var np = product * nums[i]
            if (np > limit + 1) np = limit + 1
            res = maxOf(res, dp(i + 1, np, 1, kk - nums[i]))
        }
        memo[key] = res
        return res
    }

    fun maxProduct(nums_: IntArray, k: Int, limit_: Int): Int {
        nums = nums_
        limit = limit_
        memo = HashMap()
        var sumAll = 0
        for (v in nums) sumAll += v
        if (kotlin.math.abs(k) > sumAll) return -1
        val ans = dp(0, 1, 0, k)
        return if (ans == MIN) -1 else ans
    }
}
