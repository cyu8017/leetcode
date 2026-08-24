// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

class Solution {
    fun countTrapezoids(points: Array<IntArray>): Int {
        val MOD = 1_000_000_007
        var cnt = HashMap<Int, Int>()
        for (p in points) { cnt.merge(p[1], 1, { a, b -> a + b }) }
        var ans = 0
        var pre = 0
        for (c in cnt.values) {
            var lines = c * (c - 1) / 2
            ans = (ans + pre * lines) % MOD
            pre = (pre + lines) % MOD
        }
        return ans
    }
}
