// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution {
    fun kConcatenationMaxSum(arr: IntArray, k: Int): Int {
        val MOD = 1_000_000_007L
        val one = kadane(arr)
        if (k == 1) return (one % MOD).toInt()
        val twice = IntArray(arr.size * 2)
        System.arraycopy(arr, 0, twice, 0, arr.size)
        System.arraycopy(arr, 0, twice, arr.size, arr.size)
        val two = kadane(twice)
        var total = 0L
        for (x in arr) total += x
        val ans = if (total > 0) maxOf(one, two + total * (k - 2)) else maxOf(one, two)
        return (ans % MOD).toInt()
    }

    private fun kadane(nums: IntArray): Long {
        var best = 0L
        var cur = 0L
        for (x in nums) {
            cur = maxOf(0L, cur + x)
            best = maxOf(best, cur)
        }
        return best
    }
}
