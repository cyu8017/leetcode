// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution {
    private fun gcdll(a: Long, b: Long): Long {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }

    private fun lcmll(a: Long, b: Long): Long {
        return a / gcdll(a, b) * b
    }

    private fun bitCount(x: Int): Int {
        var c = 0
        while (x != 0) {
            c += x & 1
            x >>= 1
        }
        return c
    }

    fun findKthSmallest(coins: IntArray, k: Int): Long {
        var r = 100000000000L
        var n = coins.size
        var lo = 1
        var hi = r
        while (lo < hi) {
            var mid = lo + (hi - lo) / 2
            if (check(coins, n, mid, k)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun check(coins: IntArray, n: Int, mx: Long, k: Int): Boolean {
        var cnt = 0
        for (i in 1 until (1  shl  n)) {
            var v = 1
            for (j in 0 until n) {
                if (((i  shr  j) & 1) != 0) {
                    v = lcmll(v, coins[j])
                    if (v > mx) break
                }
            }
            var m = bitCount(i)
            if (m % 2 == 1) cnt += mx / v
            else cnt -= mx / v
        }
        return cnt >= k
    }
}
