// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

class Solution {
    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        val mod = 1000000007L
        val points = n + 1
        val values = LongArray(points + 1)
        for (m in 1..points) {
            var up = LongArray(m)
            var down = LongArray(m)
            for (value in 0 until m) {
                up[value] = value.toLong()
                down[value] = (m - 1 - value).toLong()
            }
            for (length in 3..n) {
                val nextUp = LongArray(m)
                val nextDown = LongArray(m)
                var prefix = 0L
                for (value in 0 until m) {
                    nextUp[value] = prefix
                    prefix = (prefix + down[value]) % mod
                }
                var suffix = 0L
                for (value in m - 1 downTo 0) {
                    nextDown[value] = suffix
                    suffix = (suffix + up[value]) % mod
                }
                up = nextUp
                down = nextDown
            }
            for (value in 0 until m) {
                values[m] = (values[m] + up[value] + down[value]) % mod
            }
        }
        val x = ((r - l + 1) % mod + mod) % mod
        if (r - l + 1 <= points) return values[r - l + 1].toInt()
        val prefixA = LongArray(points + 2)
        val suffixA = LongArray(points + 2)
        prefixA[0] = 1
        for (i in 1..points) {
            prefixA[i] = prefixA[i - 1] * ((x - i + mod) % mod) % mod
        }
        suffixA[points + 1] = 1
        for (i in points downTo 1) {
            suffixA[i] = suffixA[i + 1] * ((x - i + mod) % mod) % mod
        }
        val factorial = LongArray(points + 1)
        factorial[0] = 1
        for (i in 1..points) factorial[i] = factorial[i - 1] * i % mod
        var answer = 0L
        for (i in 1..points) {
            val numerator = prefixA[i - 1] * suffixA[i + 1] % mod
            val denominator = factorial[i - 1] * factorial[points - i] % mod
            val term = values[i] * numerator % mod * powm(denominator, mod - 2, mod) % mod
            if ((points - i) % 2 == 1) answer -= term
            else answer += term
            answer %= mod
        }
        if (answer < 0) answer += mod
        return answer.toInt()
    }

    private fun powm(a0: Long, e0: Long, mod: Long): Long {
        var a = a0
        var e = e0
        var res = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) res = res * a % mod
            a = a * a % mod
            e = e shr 1
        }
        return res
    }
}
