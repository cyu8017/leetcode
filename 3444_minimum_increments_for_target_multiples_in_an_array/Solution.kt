// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

class Solution {
    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }

    private fun lcm(a: Int, b: Int): Int = a / gcd(a, b) * b

    fun minimumIncrements(nums: IntArray, target: IntArray): Int {
        val m = target.size
        val N = 1 shl m
        val inf = 1e18.toLong()
        var dp = LongArray(N) { inf }
        dp[0] = 0
        for (x in nums) {
            val ndp = dp.copyOf()
            for (mask in 0 until N) {
                for (sub in 1 until N) {
                    var L = 1
                    var ok = true
                    for (i in 0 until m) {
                        if ((sub and (1 shl i)) != 0) {
                            L = lcm(L, target[i])
                            if (L > 1_000_000_000) {
                                ok = false
                                break
                            }
                        }
                    }
                    if (!ok) continue
                    val cost = (L - x % L) % L
                    val nmask = mask or sub
                    if (dp[mask] + cost < ndp[nmask]) ndp[nmask] = dp[mask] + cost
                }
            }
            dp = ndp
        }
        return dp[N - 1].toInt()
    }
}
