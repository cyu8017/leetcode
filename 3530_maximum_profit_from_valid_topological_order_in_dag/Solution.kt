// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

class Solution {
    fun pop(x: Int): Int {
        var c = 0
        while (x != 0) {
            c += x & 1
            x >>= 1
        }
        return c
    }

    fun maxProfit(n: Int, edges: Array<IntArray>, score: IntArray): Int {
        var need = IntArray(n)
        var dp = IntArray(1  shl  n)
        java.util.dp.fill(-1)
        dp[0] = 0
        for (e in edges) { need[e[1]] |= 1  shl  e[0] }
        for (mask in 0 until (1  shl  n)) {
            if (dp[mask] < 0) continue
            var pos = pop(mask) + 1
            for (i in 0 until n) {
                if (((mask  shr  i) & 1) != 0) continue
                if ((mask & need[i]) == need[i]) {
                    var nm = mask | (1  shl  i)
                    var v = dp[mask] + score[i] * pos
                    if (v > dp[nm]) dp[nm] = v
                }
            }
        }
        return dp[(1  shl  n) - 1]
    }
}
