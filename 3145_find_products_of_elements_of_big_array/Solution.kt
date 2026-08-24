// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

class Solution {
    private val M: Int = 50
    private val cnt: LongArray = LongArray(M + 1)
    private val s: LongArray = LongArray(M + 1)

    constructor() {
        var p = 1
        cnt[0] = 0
        s[0] = 0
        for (i in 1 until = M) {
            cnt[i] = cnt[i - 1] * 2 + p
            s[i] = s[i - 1] * 2 + p * (i - 1)
            p *= 2
        }
    }

    private fun numIdxAndSum(x: Long): LongArray {
        var idx = 0
        var totalSum = 0
        while (x > 0) {
            var i = 63 - Long.numberOfLeadingZeros(x)
            idx += cnt[i]
            totalSum += s[i]
            x -= 1L  shl  i
            totalSum += (x + 1) * i
            idx += x + 1
        }
        return longArrayOf(idx, totalSum)
    }

    private fun f(i: Long): Long {
        var l = 0
        var r = 1L  shl  M
        while (l < r) {
            var mid = (l + r + 1)  shr  1
            var p = numIdxAndSum(mid)
            if (p[0] < i) l = mid
            else r = mid - 1
        }
        var p = numIdxAndSum(l)
        var totalSum = p[1]
        i -= p[0]
        var x = l + 1
        for (j in 0 until i) {
            var y = x & -x
            totalSum += Long.numberOfTrailingZeros(y)
            x -= y
        }
        return totalSum
    }

    private fun qpow(a: Long, n: Long, mod: Long): Long {
        var ans = 1 % mod
        a %= mod
        while (n > 0) {
            if ((n & 1) != 0) ans = ans * a % mod
            a = a * a % mod
            n >>= 1
        }
        return ans
    }

    fun findProductsOfElements(queries: Array<LongArray>): IntArray {
        var ans = IntArray(queries.size)
        for (i in 0 until queries.size) {
            var left = queries[i][0]
            var right = queries[i][1]
            var mod = queries[i][2]
            var power = f(right + 1) - f(left)
            ans[i] = qpow(2, power, mod)
        }
        return ans
    }
}
