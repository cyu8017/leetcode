// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
    private val MOD: Int = 1_000_000_007

    fun monkeyMove(n: Int): Int {
        return (powMod(2, n) - 2 + MOD) % MOD
    }

    private fun powMod(a: Long, e: Int): Int {
        var res = 1
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD
            a = a * a % MOD
            e >>= 1
        }
        return res
    }
}
