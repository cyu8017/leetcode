// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

class Solution {
    fun minMoves(balance: IntArray): Long {
        var sum = 0
        for (b in balance) { sum += b }
        if (sum < 0) return -1

        var n = balance.size
        var mn = balance[0]
        var idx = 0
        for (i in 1 until n) {
            if (balance[i] < mn) {
                mn = balance[i]
                idx = i
            }
        }
        if (mn >= 0) return 0

        var need = -mn
        var ans = 0
        for (j in 1 until n) {
            var a = balance[(idx - j + n) % n]
            var b = balance[(idx + j) % n]
            var c1 = minOf(a, need)
            need -= c1
            ans += c1 * j
            var c2 = minOf(b, need)
            need -= c2
            ans += c2 * j
        }
        return ans
    }
}
